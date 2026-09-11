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
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def scaffold(bookname: str) -> None:
    BOOK = bookname
    PIPE = os.path.join(ROOT, ".space", "pipeline", BOOK)
    BACKLOG = os.path.join(ROOT, ".space", "backlog", "epic", BOOK)

    plan_path = os.path.join(BACKLOG, "book.json")
    if not os.path.exists(plan_path):
        sys.exit(f"ERROR: backlog book plan missing for '{BOOK}'. Run `/book {BOOK} init` first.")

    with open(plan_path, encoding="utf-8") as f:
        plan = json.load(f)

    chapters = plan["chapters"]
    count = len(chapters)
    filter_chain = plan["filter_chain"]
    word_target = plan.get("word_target", 500)

    os.makedirs(PIPE, exist_ok=True)

    # model.json
    model = {
        "form": "poetry",
        "book_name": BOOK,
        "book_long_title": plan["book_long_title"],
        "language": plan["language"],
        "register": "archaic/literary",
        "quality": ".framework/templates/stereotypes/poetry/qualities/aurilus.md",
        "themes": ".framework/templates/stereotypes/poetry/themes/generic.md",
        "reference": ".framework/templates/stereotypes/poetry/references/aurilus.txt",
        "index": "bookseed.txt",
        "sacred_vocabulary": {},
        "translation_guide": {},
        "chapter_count": count,
        "source_terms": [c["chapter_title"] for c in chapters],
        "gist": plan["gist"],
        "book_summary": plan["book_summary"],
        "created_at": plan["created_at"],
    }
    with open(os.path.join(PIPE, "model.json"), "w", encoding="utf-8") as f:
        json.dump(model, f, indent=2, ensure_ascii=False)

    # bookseed.txt
    with open(os.path.join(PIPE, "bookseed.txt"), "w", encoding="utf-8") as f:
        for c in chapters:
            f.write(c["chapter_title"] + "\n")

    # book.json (pipeline clone)
    with open(os.path.join(PIPE, "book.json"), "w", encoding="utf-8") as f:
        json.dump(plan, f, indent=2, ensure_ascii=False)

    # override.txt (default)
    with open(os.path.join(PIPE, "override.txt"), "w", encoding="utf-8") as f:
        f.write("No transform required.\n")

    # progress.json
    progress = {
        "title": plan["book_long_title"],
        "language": plan["language"],
        "source_terms": [c["chapter_title"] for c in chapters],
        "context": "../context/qualities/aurilus.md + writer.md",
        "total_chapters": count,
        "completed_chapters": 0,
        "current_chapter": 1,
        "chapters": [
            {
                "chapter_number": c["chapter_index"],
                "topic": c["chapter_title"],
                "category": "The Woman Who Is Delhi",
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
            f.write(f"# {name} Filter Summary\n\n(Not yet run.)\n")
        with open(os.path.join(fd, "content-input.md"), "w", encoding="utf-8") as f:
            f.write(f"# {name} Content Input\n\n(Snapshot of the upstream input this filter consumed. Populated when the filter runs; used for undo/rollback.)\n")
        with open(os.path.join(fd, "content-output.md"), "w", encoding="utf-8") as f:
            f.write(f"# {name} Content Output\n\n(Not yet run.)\n")

    # override command file
    with open(os.path.join(filters_dir, "override", "filter.md"), "w", encoding="utf-8") as f:
        f.write(f"# {BOOK} poetry override command file\n\n")
        f.write(f"Applies to every poem in the {BOOK} pipeline. The operative form is flat, continuous poetic prose. Add transformation instructions below.\n\n")
        f.write("---\n\n## Instructions\n")

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

        cm = {
            "level": "chapter",
            "state": "scaffolded",
            "chapter_index": n,
            "chapter_name": str(n),
            "topic": c["chapter_title"],
            "chapter_title": c["chapter_title"],
            "chapter_summary": c["chapter_summary"],
            "word_target": c.get("word_target", word_target),
            "segments": [1],
        }
        with open(os.path.join(cd, "model.json"), "w", encoding="utf-8") as f:
            json.dump(cm, f, indent=2, ensure_ascii=False)

        sm = {"level": "segment", "state": "returning", "chapter_index": n, "segment_index": 1}
        with open(os.path.join(seg, "model.json"), "w", encoding="utf-8") as f:
            json.dump(sm, f, indent=2, ensure_ascii=False)

        with open(os.path.join(cd, "chapter.md"), "w", encoding="utf-8") as f:
            f.write(f"# {c['chapter_title']}\n\n")
            f.write(f"{c['chapter_summary']}\n")

    # source destination
    os.makedirs(os.path.join(ROOT, "source", "books", BOOK, "chapters"), exist_ok=True)

    print(f"Scaffolded {BOOK}: {count} chapters, filter chain {filter_chain}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: python .tools/scaffold_poetry.py <bookname>")
    scaffold(sys.argv[1])
