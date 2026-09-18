#!/usr/bin/env python3
"""
Pipeline chapter writer.

Reads chapters/<n>/model.json, flattens the complete JSON into context.md,
builds a prompt from poetry.md + that context, runs it through Ollama,
and saves the result to chapters/<n>/chapter.md.

Usage:
    python .tools/write.py behula 2       # single chapter
    python .tools/write.py behula 2-5     # inclusive range
    python .tools/write.py behula 2,5,8   # list
    python .tools/write.py behula 2-5,8   # mixed
    python .tools/write.py behula all     # all chapters
    python .tools/write.py behula "*"     # all chapters (quote the wildcard)
"""

import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
# Repo root is one level above .tools/
REPO_ROOT = BASE_DIR.parent
# The single-page Pijush/Dehlij master prompt lives in the framework.
POETRY_FILE = REPO_ROOT / ".framework" / "templates" / "styles" / "pijush" / "poetry.md"
STYLE_FILE = REPO_ROOT / ".framework" / "templates" / "styles" / "pijush" / "goddo.txt"
SUBJECTS_FILE = REPO_ROOT / ".framework" / "templates" / "stereotypes" / "poetry" / "syntax" / "gosai_bangla.md"
MODEL = "gemma4:latest"
CONTEXT_WINDOW = 64000  # num_ctx: token context window size
TEMPERATURE = 0.7      # low temperature for focused, consistent output
TOP_P = 0.9            # nucleus sampling

# Optional system prompt guiding the model's Bengali poetic persona.
# Kept tight and non-redundant: each directive covers a single concern.
SYSTEM_PROMPT = (
    "তুমি বাংলা সাহিত্যের একজন সংবেদনশীল, সৃজনশীল ও দক্ষ কবি-সম্পাদক। "
    "তোমার কাজ মননশীল, ভাবগম্ভীর ও হৃদয়গ্রাহী বাংলা কবিতা রচনা করা।\n\n"
    "নির্দেশাবলি:\n"
    "১. ভাষা ও শৈলী: প্রাঞ্জল, কাব্যিক ও সমৃদ্ধ বাংলা শব্দচয়ন ব্যবহার করো। "
    "অপ্রয়োজনীয় ইংরেজি শব্দ, গতানুগতিক পুনরাবৃত্তি এবং যান্ত্রিক বাক্যরীতি এড়িয়ে চলো। "
    "প্রম্পটের চাহিদা অনুযায়ী চলিত/সাধু/কথ্য—যেকোনো এক রীতির ধারাবাহিকতা বজায় রাখো।\n"
    "২. ভাব ও গভীরতা: শব্দে থাকুক গভীর আবেগ, রূপক ও চিন্তার খোরাক; "
    "প্রতিটি পঙ্‌ক্তি সৃজনশীল, মৌলিক ও পাঠকের মনে গভীর ছাপ ফেলার মতো হোক—ক্লিশে এড়িয়ে চলো।\n"
    "৩. সম্পাদনা: লেখার পর প্রয়োজনে নিজেই পঙ্‌ক্তিবিন্যাস, অন্ত্যমিল ও শব্দের দ্যোতনা যাচাই করে "
    "পরিশীলিত রূপ দাও—একবার লিখে শেষ নয়, প্রয়োজনে পুনর্লিখন করো।\n"
    "৪. আউটপুট: শুধু কবিতার মূল অংশ লিখো; শিরোনাম, মার্কডাউন কোড ব্লক বা ভূমিকা দিও না "
    "(যদি না নির্দেশ দেওয়া হয়)।"
)

# Use 127.0.0.1 (IPv4) explicitly. On this machine "localhost" resolves to
# ::1 (IPv6) first, which hits a *different* Ollama server (native Windows)
# that does NOT have the `writer-gemma` model. The WSL Ollama instance that
# does host `writer-gemma` is bound to 127.0.0.1 only.
OLLAMA_URL = "http://127.0.0.1:11434/api/generate"
TIMEOUT = 900  # seconds; long chapters can take a while

ANSI_RE = re.compile(r"\x1b\[[0-9;]*[A-Za-z]")

VERBOSE = False
SHOW_PROMPT = False

# Retry behaviour for transient Ollama failures.
MAX_RETRIES = 3
RETRY_DELAY = 5.0  # seconds between attempts (linear backoff)


def vlog(*args) -> None:
    """Print a verbose-only message (prefixed with a dim '[v]' marker)."""
    if VERBOSE:
        print("[v]", *args)


def info(*args) -> None:
    print(*args)


def parse_chapter_input(value: str, chapters_root: Path | None = None) -> list[int]:
    """Parse numbers/ranges, or discover all numeric chapter folders in order."""
    if value.strip().lower() in {"all", "*"}:
        if chapters_root is None:
            raise ValueError("A chapters directory is required for all or '*'")
        numbers = sorted({
            int(folder.name)
            for folder in chapters_root.iterdir()
            if folder.is_dir() and re.fullmatch(r"[0-9]+", folder.name)
            and int(folder.name) > 0
        })
        if not numbers:
            raise ValueError(f"No numbered chapters found in {chapters_root}")
        return numbers
    numbers = []
    for token in value.split(","):
        match = re.fullmatch(r"([0-9]+)(?:-([0-9]+))?", token.strip())
        if match is None:
            raise ValueError("Expected all, '*', or chapter numbers, e.g. 2, 2-5, or 2-5,8")
        start = int(match.group(1))
        end = int(match.group(2)) if match.group(2) else start
        if start < 1 or end < start:
            raise ValueError("Chapter numbers must be positive and ranges ascending")
        numbers.extend(range(start, end + 1))
    return list(dict.fromkeys(numbers))


def resolve_chapters_root(bookname: str) -> Path:
    """Resolve a book folder relative to this script's repository root."""
    if not bookname.strip() or bookname in {".", ".."} or any(
        char in bookname for char in '/\\:<>"|?*'
    ):
        raise ValueError("Bookname must be a single pipeline folder name")
    chapters_root = REPO_ROOT / ".space" / "pipeline" / bookname / "chapters"
    if not chapters_root.is_dir():
        raise ValueError(f"Chapters directory not found: {chapters_root}")
    return chapters_root


def load_poetry() -> str:
    vlog(f"Loading poetry prompt from: {POETRY_FILE}")
    if not POETRY_FILE.exists():
        raise FileNotFoundError(f"Poetry prompt file not found: {POETRY_FILE}")
    text = POETRY_FILE.read_text(encoding="utf-8")
    vlog(f"  poetry.md loaded: {len(text)} chars, {text.count(chr(10)) + 1} lines")
    return text


def load_style() -> str:
    """Load the good-sample style reference (goddo.txt) for few-shot guidance."""
    vlog(f"Loading style sample from: {STYLE_FILE}")
    if not STYLE_FILE.exists():
        vlog(f"  style sample not found, continuing without it")
        return ""
    text = STYLE_FILE.read_text(encoding="utf-8")
    vlog(f"  style sample loaded: {len(text)} chars, {text.count(chr(10)) + 1} lines")
    return text


def load_subjects() -> str:
    """Load thematic subjects from gosai_bangla.md for aligned generation."""
    vlog(f"Loading subjects from: {SUBJECTS_FILE}")
    if not SUBJECTS_FILE.exists():
        vlog(f"  subjects file not found, continuing without it")
        return ""
    text = SUBJECTS_FILE.read_text(encoding="utf-8")
    vlog(f"  subjects loaded: {len(text)} chars, {text.count(chr(10)) + 1} lines")
    return text


def build_system_prompt() -> str:
    """Combine the base persona directive with style and subject references."""
    style = load_style()
    subjects = load_subjects()
    parts = [SYSTEM_PROMPT]
    if subjects:
        parts.append(
            "\n\nথিম-নির্দেশনা (বিষয়ভিত্তিক রেফারেন্স): নিচের বিষয়বস্তু কাঠামো, রূপক পরিবার "
            "এবং পবিত্র শব্দগুলির সাথে সামঞ্জস্যপূর্ণ থাকো, যেন রচনা নির্দিষ্ট থিমের "
            "মর্মবাণী প্রতিফলিত করে।\n\n"
            + subjects
        )
    if style:
        parts.append(
            "\n\nশৈলী-নির্দেশনা (রেফারেন্স নমুনা): নিচের নমুনার বাক্যগঠন, ছন্দ, রূপক ও গাম্ভীর্য "
            "অনুসরণ করো, কিন্তু এর শব্দ বা বিষয়বস্তু হুবহু নকল করবে না।\n\n"
            + style
        )
    return "".join(parts)


def flatten_json_to_markdown(data: object) -> str:
    """Render every JSON leaf with its unambiguous JSON path as a heading."""
    sections = ["# Chapter model context"]

    def visit(value: object, path: str) -> None:
        if isinstance(value, dict) and value:
            for key, child in value.items():
                visit(child, f"{path}[{json.dumps(key, ensure_ascii=False)}]")
        elif isinstance(value, list) and value:
            for index, child in enumerate(value):
                visit(child, f"{path}[{index}]")
        else:
            # JSON encoding preserves types, empty containers, and string escapes.
            rendered = json.dumps(value, ensure_ascii=False, indent=2)
            # Use a fence longer than any backtick run in user-authored values.
            fence = "`" * max(3, 1 + max(
                (len(run) for run in re.findall(r"`+", rendered)), default=0
            ))
            sections.append(f"## {path}\n\n{fence}json\n{rendered}\n{fence}")

    visit(data, "$")
    return "\n\n".join(sections) + "\n"


def load_context(model_file: Path) -> str:
    """Flatten the entire model, save context.md beside it, and return Markdown."""
    data = json.loads(model_file.read_text(encoding="utf-8-sig"))
    context = flatten_json_to_markdown(data)
    context_file = model_file.with_name("context.md")
    context_file.write_text(context, encoding="utf-8")
    vlog(f"Context saved -> {context_file} ({len(context)} chars)")
    return context


def build_prompt(poetry: str, context: str, number: int) -> str:
    """Use the complete model context, including nested filter guidance."""
    prompt = (
        f"{poetry}\n\n---\n\n"
        f"Now write chapter {number}. "
        "Use the complete chapter model context below: its title, summary, "
        "word target, references, themes, and any nested enrichment or filter "
        "guidance that is present. Metadata describes the chapter; do not "
        "reproduce JSON paths, state fields, or context headings in the output. "
        "Embody the philosophy, voice, and structure defined above, and "
        "match the syntax and rhythm of the sample above. "
        "Write in poetic prose (Bengali), no headings, no markdown code blocks, "
        "no title unless asked.\n\n"
        f"CHAPTER CONTEXT (complete model.json):\n\n{context}"
    )
    vlog(f"[{number}] Final prompt size: {len(prompt)} chars "
         f"({len(prompt.encode('utf-8'))} bytes UTF-8)")
    return prompt


def strip_ansi(text: str) -> str:
    """Remove ANSI escape sequences (cursor/color codes) from text."""
    return ANSI_RE.sub("", text)


def run_ollama(prompt: str) -> str:
    """Call Ollama's HTTP API directly and return the generated text.

    Uses ``think=False`` to suppress the model's internal reasoning/"thinking"
    output, and ``stream=False`` so the result is plain text (no ANSI codes).
    Retries transient failures with linear backoff.
    """
    payload = {
        "model": MODEL,
        "prompt": prompt,
        "system": build_system_prompt(),
        "stream": False,
        "think": False,
        "options": {
            "num_ctx": CONTEXT_WINDOW,
            "temperature": TEMPERATURE,
            "top_p": TOP_P,
        },
    }
    vlog(f"[ollama] POST {OLLAMA_URL} model='{MODEL}' think=False stream=False "
         f"num_ctx={CONTEXT_WINDOW} temperature={TEMPERATURE} top_p={TOP_P}")

    encoded = json.dumps(payload).encode("utf-8")
    vlog(f"[ollama] Sending prompt ({len(prompt)} chars)")

    last_error = None
    for attempt in range(1, MAX_RETRIES + 1):
        req = urllib.request.Request(
            OLLAMA_URL,
            data=encoded,
            headers={"Content-Type": "application/json"},
        )
        t0 = time.time()
        try:
            with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
                body = resp.read().decode("utf-8")
        except (urllib.error.URLError, TimeoutError) as e:
            last_error = e
            vlog(f"[ollama] attempt {attempt}/{MAX_RETRIES} failed: {e}")
            if attempt < MAX_RETRIES:
                delay = RETRY_DELAY * attempt
                vlog(f"[ollama] retrying in {delay:.1f}s ...")
                time.sleep(delay)
                continue
            raise RuntimeError(f"Ollama request failed after {MAX_RETRIES} attempts: {e}") from e

        elapsed = time.time() - t0
        vlog(f"[ollama] Completed in {elapsed:.2f}s (attempt {attempt})")
        data = json.loads(body)
        response = data.get("response", "")
        thinking = data.get("thinking", "")
        vlog(f"[ollama] response size: {len(response)} chars, "
             f"thinking size: {len(thinking)} chars")

        # Safety net: strip any stray ANSI escape sequences that leak through.
        cleaned = strip_ansi(response)
        if cleaned != response:
            vlog(f"[ollama] Removed {len(response) - len(cleaned)} ANSI escape chars")
        return cleaned.strip()

    # Unreachable; kept for type-safety/clarity.
    raise RuntimeError(f"Ollama request failed: {last_error}")


def write_chapter(model_file: Path) -> None:
    number = int(model_file.parent.name)
    info(f"\n=== Chapter {number} ===")
    chapter_dir = model_file.parent
    vlog(f"[{number}] Chapter dir ready: {chapter_dir}")

    poetry = load_poetry()
    context = load_context(model_file)
    prompt = build_prompt(poetry, context, number)

    if SHOW_PROMPT:
        info(f"\n[{number}] ============ COMPLETE REQUEST ============")
        info(f"[{number}] model      = {MODEL}")
        info(f"[{number}] num_ctx    = {CONTEXT_WINDOW}")
        info(f"[{number}] temperature= {TEMPERATURE}")
        info(f"[{number}] top_p      = {TOP_P}")
        info(f"[{number}] think      = False, stream = False")
        sys_prompt = build_system_prompt()
        info(f"\n[{number}] ----- SYSTEM PROMPT ({len(sys_prompt)} chars) -----")
        info(sys_prompt)
        info(f"[{number}] ----- END SYSTEM PROMPT -----")
        info(f"\n[{number}] ----- PROMPT ({len(prompt)} chars) -----")
        info(prompt)
        info(f"[{number}] ----- END PROMPT -----")
        info(f"[{number}] ============ END REQUEST ============\n")

    info(f"[{number}] Generating chapter from complete model context ...")
    t0 = time.time()
    output = run_ollama(prompt)
    elapsed = time.time() - t0

    out_file = chapter_dir / "chapter.md"
    out_file.write_text(output + "\n", encoding="utf-8")
    word_count = len(output.split())
    vlog(f"[{number}] Output: {len(output)} chars, ~{word_count} words")
    info(f"[{number}] Saved -> {out_file} "
         f"({len(output)} chars in {elapsed:.2f}s)")


def main() -> int:
    global VERBOSE, SHOW_PROMPT
    parser = argparse.ArgumentParser(
        description="Generate pipeline chapters via Ollama.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""Examples:
  python .tools/write.py behula 2          Single chapter
  python .tools/write.py behula 2-5        Inclusive range
  python .tools/write.py behula 2,5,8      Chapter list
  python .tools/write.py behula 2-5,8      Range and list combined
  python .tools/write.py behula all        All numbered chapters, in order
  python .tools/write.py behula "*"        All chapters (quote the wildcard)
  python .tools/write.py behula 2 -v      Verbose logging
  python .tools/write.py behula 2 -p      Show prompt, then generate
  python .tools/write.py help             Show this help
  python .tools/write.py --help           Show this help (also -h)

Input:  .space/pipeline/<bookname>/chapters/<n>/model.json
Context: .space/pipeline/<bookname>/chapters/<n>/context.md (regenerated from full JSON)
Output: .space/pipeline/<bookname>/chapters/<n>/chapter.md
Paths are resolved relative to the repository, regardless of your current directory.
""",
    )
    parser.add_argument("bookname", help="Book folder under .space/pipeline/.")
    parser.add_argument(
        "chapters",
        help="Chapter number, range, list (2, 2-5, 2-5,8), all, or '*'.",
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose logging.",
    )
    parser.add_argument(
        "-p", "--show-prompt",
        action="store_true",
        help="Print the full prompt to stdout before invoking Ollama.",
    )
    if sys.argv[1:] == ["help"]:
        parser.print_help()
        return 0
    args = parser.parse_args()
    VERBOSE = args.verbose
    SHOW_PROMPT = args.show_prompt

    vlog(f"BASE_DIR       = {BASE_DIR}")
    vlog(f"POETRY_FILE    = {POETRY_FILE}")
    vlog(f"MODEL          = {MODEL}")
    vlog(f"Verbose mode   = {VERBOSE}")

    try:
        chapters_root = resolve_chapters_root(args.bookname)
        numbers = parse_chapter_input(args.chapters, chapters_root)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

    info(f"Processing {args.bookname}: {len(numbers)} chapter(s): {numbers}")
    failures = 0
    for number in numbers:
        model_file = chapters_root / str(number) / "model.json"
        try:
            write_chapter(model_file)
        except Exception as e:
            print(f"[{number}] FAILED: {e}", file=sys.stderr)
            failures += 1
    info(f"Done. {len(numbers) - failures} succeeded, {failures} failed.")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
