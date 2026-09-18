#!/usr/bin/env python3
"""Test client for the Novelist Book MCP server (``.tools/book_server.py``).

Exercises the MCP tools over stdio JSON-RPC, mirroring the pattern in
``.tools/test_searxng_client.py``. Requires the HTTP publish service to be
running first:

    python .tools/db/publish_api.py

Then run:

    python bt.py
"""
import json
import os
import subprocess
import sys
import time

REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
SERVER = os.path.join(REPO_ROOT, ".tools", "book_server.py")

# Use an existing book in the repo for read-only checks, so the test is
# non-destructive by default. Override via BOOK_NAME to target another book.
BOOK_NAME = os.environ.get("BOOK_NAME", "behula")


def send(proc, obj):
    line = json.dumps(obj, ensure_ascii=False) + "\n"
    proc.stdin.write(line)
    proc.stdin.flush()


def readline(proc, timeout=15):
    start = time.time()
    while time.time() - start < timeout:
        line = proc.stdout.readline()
        if line:
            return line.strip()
        time.sleep(0.05)
    raise TimeoutError("No response from server")


def call_tool(proc, name, arguments, call_id):
    send(
        proc,
        {
            "jsonrpc": "2.0",
            "id": call_id,
            "method": "tools/call",
            "params": {"name": name, "arguments": arguments},
        },
    )
    line = readline(proc)
    payload = json.loads(line)
    if "error" in payload:
        raise RuntimeError(f"tool '{name}' returned error: {payload['error']}")
    result = payload.get("result", {})
    content = result.get("content", [])
    if not content:
        return None
    text = content[0].get("text", "")
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return text


def main():
    proc = subprocess.Popen(
        [sys.executable, SERVER],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        bufsize=1,
        env=os.environ.copy(),
    )

    try:
        # 1. initialize handshake
        print("[1] initialize...")
        send(
            proc,
            {
                "jsonrpc": "2.0",
                "id": 1,
                "method": "initialize",
                "params": {
                    "protocolVersion": "2024-11-05",
                    "capabilities": {},
                    "clientInfo": {"name": "book-test", "version": "0.1.0"},
                },
            },
        )
        init_resp = json.loads(readline(proc))
        assert "result" in init_resp, f"init failed: {init_resp}"
        print("    server:", init_resp["result"]["serverInfo"]["name"])

        send(proc, {"jsonrpc": "2.0", "method": "notifications/initialized"})

        # 2. list tools
        print("[2] tools/list...")
        send(proc, {"jsonrpc": "2.0", "id": 2, "method": "tools/list", "params": {}})
        tools_line = readline(proc)
        tools = json.loads(tools_line)["result"]["tools"]
        tool_names = sorted(t["name"] for t in tools)
        print("    tools:", tool_names)
        expected = [
            "add_chapter",
            "create_book",
            "delete_chapter",
            "edit_book",
            "edit_chapter",
            "get_book",
            "get_chapter",
            "get_chapter_content",
            "get_chapter_content_by_version",
            "list_chapters",
            "list_versions",
            "publish",
        ]
        for name in expected:
            assert name in tool_names, f"missing tool '{name}'"

        # 3. read-only sample: get_book
        print(f"[3] get_book('{BOOK_NAME}')...")
        book = call_tool(proc, "get_book", {"book_name": BOOK_NAME}, 3)
        assert isinstance(book, dict) and "book_name" in book, f"unexpected: {book}"
        print(f"    title: {book.get('book_long_title', book.get('book_name'))}")

        # 4. read-only sample: list_chapters
        print(f"[4] list_chapters('{BOOK_NAME}')...")
        chapters = call_tool(proc, "list_chapters", {"book_name": BOOK_NAME}, 4)
        assert isinstance(chapters, list), f"unexpected: {chapters}"
        print(f"    chapter count: {len(chapters)}")

        # 5. read-only sample: get_chapter + get_chapter_content
        if chapters:
            first = str(chapters[0].get("chapter_index", chapters[0].get("name", "1")))
            print(f"[5] get_chapter('{BOOK_NAME}', '{first}')...")
            meta = call_tool(proc, "get_chapter", {"book_name": BOOK_NAME, "chapter": first}, 5)
            assert isinstance(meta, dict), f"unexpected: {meta}"
            print(f"    topic: {meta.get('topic', meta.get('chapter_title', ''))}")

            print(f"[6] get_chapter_content('{BOOK_NAME}', '{first}')...")
            content = call_tool(proc, "get_chapter_content", {"book_name": BOOK_NAME, "chapter": first}, 6)
            assert isinstance(content, str) and len(content) > 0, "no content returned"
            print(f"    content length: {len(content)} chars")

        # 6. read-only sample: list_versions
        print(f"[7] list_versions('{BOOK_NAME}')...")
        versions = call_tool(proc, "list_versions", {"book_name": BOOK_NAME}, 7)
        assert isinstance(versions, list), f"unexpected: {versions}"
        print(f"    versions: {versions}")

        print("\nAll checks passed.")
    finally:
        proc.terminate()
        try:
            proc.wait(timeout=2)
        except subprocess.TimeoutExpired:
            proc.kill()


if __name__ == "__main__":
    main()
