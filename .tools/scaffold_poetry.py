#!/usr/bin/env python3
"""
Reusable poetry-pipeline scaffold tool.

Builds the full `.space/pipeline/<bookname>/` structure from the backlog
book plan (`.space/backlog/epic/<bookname>/book.json`), following the
layout-poetry skill's canonical folder shape.

Usage:
    python .tools/scaffold_poetry.py <bookname>

The book plan (book.json) must already exist (run `/book <bookname> init` first).
"""
import json
import os
import shutil
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def scaffold(bookname: str) -> None:
    if not bookname or bookname in {".", ".."} or any(c in bookname for c in '/\\:<>"|?*'):
        sys.exit("ERROR: expected a single book folder name")
    BOOK = bookname
    PIPE = os.path.join(ROOT, ".space", "pipeline", BOOK)
    BACKLOG = os.path.join(ROOT, ".space", "backlog", "epic", BOOK)

    plan_path = os.path.join(BACKLOG, "book.json")
    if not os.path.exists(plan_path):
        sys.exit(f"ERROR: backlog book plan missing for '{BOOK}'. Run `/book {BOOK} init` first.")

    with open(plan_path, encoding="utf-8") as f:
        plan = json.load(f)

    if os.path.exists(PIPE):
        sys.exit(f"ERROR: pipeline already exists: {PIPE}; preserving existing state.")
    if plan.get("form") != "poetry" or plan.get("book_name") != BOOK:
        sys.exit("ERROR: plan identity/form does not match the requested poetry book")
    chapters = plan["chapters"]
    if not chapters or plan.get("chapter_count") != len(chapters):
        sys.exit("ERROR: chapter count does not match the plan")
    for index, chapter in enumerate(chapters, 1):
        if type(chapter.get("chapter_index")) is not int or chapter["chapter_index"] != index or chapter.get("name") != str(index):
            sys.exit("ERROR: poetry chapter identities must be sequential")
        if type(chapter.get("word_target")) is not int or chapter["word_target"] <= 0:
            sys.exit("ERROR: chapter word_target must be a positive integer")
        if any(not isinstance(chapter.get(k), str) or not chapter[k].strip() for k in ("chapter_title", "chapter_summary")) or not isinstance(chapter.get("further_references"), list):
            sys.exit("ERROR: incomplete chapter schema")
    chain = plan.get("filter_chain", [])
    if not chain or len(set(chain)) != len(chain):
        sys.exit("ERROR: missing or duplicate filter chain")
    for name in chain:
        if not isinstance(name, str) or not name.isidentifier() or not os.path.isfile(os.path.join(ROOT, ".framework", "agents", name, "agent.md")):
            sys.exit("ERROR: invalid or missing filter agent")
    count = len(chapters)
    filter_chain = plan["filter_chain"]
    word_target = plan.get("word_target", 500)

    os.makedirs(PIPE, exist_ok=True)

    # Exact root-model clone required by the workflow.
    shutil.copyfile(plan_path, os.path.join(PIPE, "model.json"))

    # bookseed.txt
    with open(os.path.join(PIPE, "bookseed.txt"), "w", encoding="utf-8") as f:
        for c in chapters:
            f.write(c["chapter_title"] + "\n")

    # progress.json
    progress = {
        "title": plan["book_long_title"],
        "language": plan["language"],
        "source_terms": [c["chapter_title"] for c in chapters],
        "context": "model.json",
        "total_chapters": count,
        "completed_chapters": 0,
        "current_chapter": 1,
        "chapters": [
            {
                "chapter_number": c["chapter_index"],
                "topic": c["chapter_title"],
                "category": c.get("category", ""),
                "status": "pending",
                "file_path": f"chapters\\{c['chapter_index']}\\chapter.md",
                "completed_date": None,
            }
            for c in chapters
        ],
    }
    with open(os.path.join(PIPE, "progress.json"), "w", encoding="utf-8") as f:
        json.dump(progress, f, indent=2, ensure_ascii=False)

    # filters
    filters_dir = os.path.join(PIPE, "filters")
    os.makedirs(filters_dir, exist_ok=True)

    registry = {"filters": []}
    for i, name in enumerate(filter_chain, start=1):
        registry["filters"].append({
            "order": i,
            "name": name,
            "agent": f".framework/agents/{name}/agent.md",
            "summary_file": "filter-summary.md",
            "autorun": True,
        })
    with open(os.path.join(filters_dir, "filters.json"), "w", encoding="utf-8") as f:
        json.dump(registry, f, indent=2, ensure_ascii=False)

    for name in filter_chain:
        fd = os.path.join(filters_dir, name)
        os.makedirs(fd, exist_ok=True)
        with open(os.path.join(fd, f"{name}.md"), "w", encoding="utf-8") as f:
            f.write(f"# {name}\n\nRole agent: .framework/agents/{name}/agent.md\n")
        with open(os.path.join(fd, "filter.md"), "w", encoding="utf-8") as f:
            f.write(f"# {name} filter\n")
        with open(os.path.join(fd, "filter-summary.md"), "w", encoding="utf-8") as f:
            f.write("")
        with open(os.path.join(fd, "content-input.md"), "w", encoding="utf-8") as f:
            f.write("")
        with open(os.path.join(fd, "content-output.md"), "w", encoding="utf-8") as f:
            f.write("")

    # Seed the poetry command file from the responsible agent.
    if "override" in filter_chain:
        with open(os.path.join(ROOT, ".framework", "agents", "override", "agent.md"), encoding="utf-8") as f:
            override = f.read()
        override = override.replace("<bookname>", BOOK).replace("agent of the pipeline", "agent of the poetry pipeline")
        override = override.replace("every chapter", "every poem").replace("Every chapter", "Every poem")
        with open(os.path.join(filters_dir, "override", "filter.md"), "w", encoding="utf-8") as f:
            f.write(override.rstrip() + "\n\n---\n\n## Instructions\n")

    # chapters
    chapters_dir = os.path.join(PIPE, "chapters")
    os.makedirs(chapters_dir, exist_ok=True)

    for c in chapters:
        n = c["chapter_index"]
        cd = os.path.join(chapters_dir, str(n))
        os.makedirs(os.path.join(cd, "history"), exist_ok=True)
        seg = os.path.join(cd, "segments", "1")
        os.makedirs(os.path.join(seg, "writer"), exist_ok=True)
        os.makedirs(os.path.join(seg, "editor"), exist_ok=True)
        os.makedirs(os.path.join(seg, "translator"), exist_ok=True)

        cm = dict(c)
        cm.update({"level": "chapter", "state": "scaffolded", "segments": [1]})
        with open(os.path.join(cd, "model.json"), "w", encoding="utf-8") as f:
            json.dump(cm, f, indent=2, ensure_ascii=False)

        sm = {"level": "segment", "state": "returning", "chapter_index": n, "segment_index": 1}
        with open(os.path.join(seg, "model.json"), "w", encoding="utf-8") as f:
            json.dump(sm, f, indent=2, ensure_ascii=False)

        with open(os.path.join(cd, "chapter.md"), "w", encoding="utf-8") as f:
            f.write(f"# {c['chapter_title']}\n\n")
            f.write(f"{c['chapter_summary']}\n")

    # Postlayout default for a plain scaffold; never create reader-facing output.
    with open(os.path.join(PIPE, "override.txt"), "w", encoding="utf-8") as f:
        f.write("No transform required.\n")

    print(f"Scaffolded {BOOK}: {count} chapters, filter chain {filter_chain}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: python .tools/scaffold_poetry.py <bookname>")
    scaffold(sys.argv[1])
