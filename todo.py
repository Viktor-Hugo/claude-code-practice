"""간단한 TODO 관리 CLI.

사용법:
    python todo.py add "할 일 내용"
    python todo.py list
    python todo.py done <번호>
    python todo.py remove <번호>
"""

import argparse
import json
import sys
from pathlib import Path

DATA_FILE = Path(__file__).with_name("todos.json")


def load_todos():
    if not DATA_FILE.exists():
        return []
    return json.loads(DATA_FILE.read_text(encoding="utf-8"))


def save_todos(todos):
    DATA_FILE.write_text(json.dumps(todos, ensure_ascii=False, indent=2), encoding="utf-8")


def next_id(todos):
    return max((t["id"] for t in todos), default=0) + 1


def find_todo(todos, todo_id):
    for todo in todos:
        if todo["id"] == todo_id:
            return todo
    sys.exit(f"{todo_id}번 할 일을 찾을 수 없습니다.")


def cmd_add(args):
    todos = load_todos()
    todo = {"id": next_id(todos), "title": args.title, "done": False}
    todos.append(todo)
    save_todos(todos)
    print(f"추가됨: [{todo['id']}] {todo['title']}")


def cmd_list(args):
    todos = load_todos()
    if not todos:
        print("할 일이 없습니다.")
        return
    for todo in todos:
        mark = "x" if todo["done"] else " "
        print(f"[{mark}] {todo['id']}. {todo['title']}")


def cmd_done(args):
    todos = load_todos()
    todo = find_todo(todos, args.id)
    todo["done"] = True
    save_todos(todos)
    print(f"완료: [{todo['id']}] {todo['title']}")


def cmd_remove(args):
    todos = load_todos()
    todo = find_todo(todos, args.id)
    todos.remove(todo)
    save_todos(todos)
    print(f"삭제됨: [{todo['id']}] {todo['title']}")


def main():
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")

    parser = argparse.ArgumentParser(description="간단한 TODO 관리 CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    p_add = sub.add_parser("add", help="할 일 추가")
    p_add.add_argument("title", help="할 일 내용")
    p_add.set_defaults(func=cmd_add)

    p_list = sub.add_parser("list", help="할 일 목록 보기")
    p_list.set_defaults(func=cmd_list)

    p_done = sub.add_parser("done", help="할 일 완료 처리")
    p_done.add_argument("id", type=int, help="할 일 번호")
    p_done.set_defaults(func=cmd_done)

    p_remove = sub.add_parser("remove", help="할 일 삭제")
    p_remove.add_argument("id", type=int, help="할 일 번호")
    p_remove.set_defaults(func=cmd_remove)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
