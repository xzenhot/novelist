#!/usr/bin/env python3
"""Publish chapter-root drafts with titles from their chapter models.

Usage: python .tools/publish.py <bookname>
Reads only chapters/<n>/chapter.md and chapters/<n>/model.json.
Creates source/books/<bookname>/version<k>/chapters/<n>/chapter.md and book.md.
"""
import argparse
import datetime
import json
import os
import re
from pathlib import Path

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def publish(bookname: str) -> None:
    if not bookname or bookname in {".", ".."} or any(c in bookname for c in '/\\:<>"|?*'):
        raise ValueError("Expected a single book folder name")
    pipeline = Path(ROOT) / ".space" / "pipeline" / bookname
    chapters_root = pipeline / "chapters"
    if not chapters_root.is_dir():
        raise ValueError(f"Pipeline chapters missing for {bookname!r}; run scaffold first")
    model = json.loads((pipeline / "model.json").read_text(encoding="utf-8-sig"))
    progress_path = pipeline / "progress.json"
    progress = json.loads(progress_path.read_text(encoding="utf-8-sig")) if progress_path.exists() else None

    def chapter_order(folder):
        if folder.name == "Introduction":
            return (0, 0)
        if folder.name.isdecimal():
            return (1, int(folder.name))
        return (2, 0)  # Conclusion

    folders = sorted((p for p in chapters_root.iterdir() if p.is_dir() and
                      (p.name.isdecimal() or p.name in {"Introduction", "Conclusion"})),
                     key=chapter_order)
    published, skipped = [], []
    for folder in folders:
        draft = folder / "chapter.md"
        chapter_model = folder / "model.json"
        try:
            body = draft.read_text(encoding="utf-8-sig").strip()
            metadata = json.loads(chapter_model.read_text(encoding="utf-8-sig"))
            title = metadata.get("chapter_title")
            if not body:
                raise ValueError("empty chapter.md")
            if not isinstance(title, str) or not title.strip():
                raise ValueError("missing chapter_title in model.json")
            title = " ".join(title.split())
            # Replace an existing leading title; metadata is authoritative.
            lines = body.splitlines()
            if re.match(r"^#{1,6}\s+", lines[0]):
                body = "\n".join(lines[1:]).strip()
            if not body:
                raise ValueError("chapter.md contains only a heading")
            published.append((folder.name, title, body))
        except (OSError, ValueError, AttributeError) as error:
            skipped.append((folder.name, str(error)))

    for name, reason in skipped:
        print(f"Skipped chapter {name}: {reason}")
    if not published:
        raise ValueError("No usable chapter-root drafts with model titles; nothing published")

    destination = Path(ROOT) / "source" / "books" / bookname
    destination.mkdir(parents=True, exist_ok=True)
    numbers = [int(match.group(1)) for p in destination.iterdir()
               if p.is_dir() and (match := re.fullmatch(r"version([0-9]+)", p.name))]
    version = max(numbers, default=0) + 1
    while True:
        version_dir = destination / f"version{version}"
        try:
            version_dir.mkdir()
            break
        except FileExistsError:
            version += 1

    sections = []
    for name, title, body in published:
        chapter_out = version_dir / "chapters" / name
        chapter_out.mkdir(parents=True)
        (chapter_out / "chapter.md").write_text(f"# {title}\n\n{body}\n", encoding="utf-8")
        sections.append(f"## {title}\n\n{body}")
    book_title = model.get("book_long_title") or bookname
    book_file = version_dir / "book.md"
    book_file.write_text(f"# {book_title}\n\n" + "\n\n---\n\n".join(sections) + "\n", encoding="utf-8")

    if progress is not None:
        progress.update(published=not skipped,
                        published_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                        published_version=version,
                        published_chapters=[name for name, _, _ in published],
                        skipped_chapters=[name for name, _ in skipped])
        progress.pop("published_language", None)
        progress_path.write_text(json.dumps(progress, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Published {len(published)} chapters to {version_dir}; skipped {len(skipped)}")
    print(f"Assembled: {book_file}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("bookname")
    args = parser.parse_args()
    try:
        publish(args.bookname)
    except (OSError, ValueError) as error:
        parser.exit(1, f"ERROR: {error}\n")
