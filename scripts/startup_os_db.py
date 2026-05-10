import argparse
import json
import sqlite3
from datetime import date

from booskill_license import activate_license, check_license, run_cloud_core


SCHEMA = """
CREATE TABLE IF NOT EXISTS projects (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, created_at TEXT DEFAULT '', updated_at TEXT DEFAULT '');
CREATE TABLE IF NOT EXISTS team_members (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, role TEXT DEFAULT '', notes TEXT DEFAULT '', created_at TEXT DEFAULT '', updated_at TEXT DEFAULT '');
CREATE TABLE IF NOT EXISTS customers (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, owner TEXT DEFAULT '', status TEXT DEFAULT '', notes TEXT DEFAULT '', next_followup TEXT DEFAULT '', created_at TEXT DEFAULT '', updated_at TEXT DEFAULT '');
CREATE TABLE IF NOT EXISTS contacts (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, relation_type TEXT DEFAULT '', notes TEXT DEFAULT '', created_at TEXT DEFAULT '', updated_at TEXT DEFAULT '');
CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, owner TEXT DEFAULT '', due_date TEXT DEFAULT '', status TEXT DEFAULT 'todo', notes TEXT DEFAULT '', created_at TEXT DEFAULT '', updated_at TEXT DEFAULT '');
"""


def init_db(db):
    with sqlite3.connect(db) as conn:
        conn.executescript(SCHEMA)
        ensure_columns(conn)
        conn.commit()


def ensure_columns(conn):
    required = {
        "team_members": {"notes": "TEXT DEFAULT ''"},
        "customers": {"notes": "TEXT DEFAULT ''", "next_followup": "TEXT DEFAULT ''"},
        "tasks": {"notes": "TEXT DEFAULT ''"},
    }
    for table, columns in required.items():
        existing = {row[1] for row in conn.execute(f"PRAGMA table_info({table})").fetchall()}
        for column, definition in columns.items():
            if column not in existing:
                conn.execute(f"ALTER TABLE {table} ADD COLUMN {column} {definition}")


def today():
    return date.today().isoformat()


def print_json(data):
    print(json.dumps(data, ensure_ascii=False, indent=2))


def require_args(args, names):
    missing = [name for name in names if not getattr(args, name)]
    if missing:
        print_json({
            "error": "missing_required_argument",
            "missing": [f"--{name.replace('_', '-')}" for name in missing],
            "tip": "可以先运行 python scripts\\startup_os_db.py first-use-guide 查看示例。",
        })
        raise SystemExit(2)


def export_data(db):
    data = {}
    with sqlite3.connect(db) as conn:
        conn.row_factory = sqlite3.Row
        for table in ["projects", "team_members", "customers", "contacts", "tasks"]:
            data[table] = [dict(row) for row in conn.execute(f"SELECT * FROM {table}").fetchall()]
    return data


def first_use_guide():
    return """我是 BossSkill 老板经营秘书。你可以先这样用：

1. 建客户：python scripts\\startup_os_db.py add-customer --name "李总" --status "高意向" --next-followup "2026-05-12" --text "做餐饮加盟，预算5万，关心回本周期"
2. 建员工：python scripts\\startup_os_db.py add-team-member --name "张三" --role "销售" --text "执行力可以，成交话术弱"
3. 建任务：python scripts\\startup_os_db.py add-task --title "周三跟进李总预算" --owner "张三" --due-date "2026-05-12"
4. 看简报：python scripts\\startup_os_db.py daily-brief
5. 一句话老板秘书：python scripts\\startup_os_db.py assistant-action --text "今天帮我看看哪些客户需要跟进"

授权版会开放更强的老板秘书判断、行业打法、客户跟进话术、团队诊断和持续学习知识库。
授权联系 Telegram: fanfans555"""


def insert_record(db, table, values):
    keys = list(values.keys())
    placeholders = ", ".join(["?"] * len(keys))
    with sqlite3.connect(db) as conn:
        cursor = conn.execute(
            f"INSERT INTO {table} ({', '.join(keys)}) VALUES ({placeholders})",
            [values[key] for key in keys],
        )
        conn.commit()
        return cursor.lastrowid


def add_customer(db, args):
    record_id = insert_record(db, "customers", {
        "name": args.name,
        "owner": args.owner or "",
        "status": args.status or "",
        "notes": args.text or "",
        "next_followup": args.next_followup or "",
        "created_at": today(),
        "updated_at": today(),
    })
    return {
        "created": "customer",
        "id": record_id,
        "next_step": "如果知道客户生日、爱好、预算、关键顾虑，可以继续补充，后续跟进会更精准。",
    }


def add_team_member(db, args):
    record_id = insert_record(db, "team_members", {
        "name": args.name,
        "role": args.role or "",
        "notes": args.text or "",
        "created_at": today(),
        "updated_at": today(),
    })
    return {
        "created": "team_member",
        "id": record_id,
        "next_step": "建议补充这个人的强项、短板、最近任务结果，方便后续做团队诊断。",
    }


def add_contact(db, args):
    record_id = insert_record(db, "contacts", {
        "name": args.name,
        "relation_type": args.relation_type or "",
        "notes": args.text or "",
        "created_at": today(),
        "updated_at": today(),
    })
    return {
        "created": "contact",
        "id": record_id,
        "next_step": "建议补充对方能帮什么、你需要如何维护关系、生日或联系禁忌。",
    }


def add_task(db, args):
    record_id = insert_record(db, "tasks", {
        "title": args.title,
        "owner": args.owner or "",
        "due_date": args.due_date or "",
        "status": args.status or "todo",
        "notes": args.text or "",
        "created_at": today(),
        "updated_at": today(),
    })
    return {"created": "task", "id": record_id, "next_step": "任务完成后请记录结果，系统才能帮你复盘。"}


def list_table(db, table):
    allowed = {"projects", "team_members", "customers", "contacts", "tasks"}
    if table not in allowed:
        return {"error": "unsupported_table", "allowed": sorted(allowed)}
    with sqlite3.connect(db) as conn:
        conn.row_factory = sqlite3.Row
        return [dict(row) for row in conn.execute(f"SELECT * FROM {table} ORDER BY id DESC LIMIT 50").fetchall()]


def local_daily_brief(db):
    data = export_data(db)
    today_text = today()
    due_tasks = [
        task for task in data["tasks"]
        if task.get("status") != "done" and task.get("due_date") and task.get("due_date") <= today_text
    ]
    followups = [
        customer for customer in data["customers"]
        if customer.get("next_followup") and customer.get("next_followup") <= today_text
    ]
    return {
        "title": "BossSkill 今日简报",
        "today": today_text,
        "must_handle": {
            "due_tasks": due_tasks,
            "customer_followups": followups,
        },
        "counts": {
            "customers": len(data["customers"]),
            "team_members": len(data["team_members"]),
            "contacts": len(data["contacts"]),
            "tasks": len(data["tasks"]),
        },
        "suggested_action": [
            "先处理到期任务和到期客户跟进。",
            "每完成一个任务，补充完成结果。",
            "客户信息缺失时，优先补充需求、预算、顾虑和下次跟进时间。",
        ],
        "upgrade_hint": "授权版可根据客户记录生成跟进策略、话术、团队动作和经营诊断。授权联系 Telegram: fanfans555",
    }


def license_required(command):
    return {
        "intent": "license_required",
        "command": command,
        "message": "这个能力属于授权版。免费版可使用 add-customer、add-team-member、add-contact、add-task、daily-brief 和 export。",
        "activate_command": "python scripts\\startup_os_db.py activate-license --db startup_os.sqlite3 --license-key YOUR_LICENSE_KEY",
        "contact": "Telegram: fanfans555",
    }


def main():
    parser = argparse.ArgumentParser(description="BossSkill cloud client")
    parser.add_argument("command")
    parser.add_argument("--db", default="startup_os.sqlite3")
    parser.add_argument("--license-key")
    parser.add_argument("--text")
    parser.add_argument("--name")
    parser.add_argument("--owner")
    parser.add_argument("--status")
    parser.add_argument("--next-followup")
    parser.add_argument("--role")
    parser.add_argument("--relation-type")
    parser.add_argument("--title")
    parser.add_argument("--due-date")
    parser.add_argument("--table")
    args = parser.parse_args()
    init_db(args.db)
    if args.command == "init":
        print(f"initialized {args.db}")
        return
    if args.command in {"first-use-guide", "guide"}:
        print(first_use_guide())
        return
    if args.command == "activate-license":
        require_args(args, ["license_key"])
        print_json(activate_license(args.db, args.license_key))
        return
    if args.command == "license-status":
        print_json(check_license(args.db, "status"))
        return
    if args.command == "export":
        print_json(export_data(args.db))
        return
    if args.command == "add-customer":
        require_args(args, ["name"])
        print_json(add_customer(args.db, args))
        return
    if args.command == "add-team-member":
        require_args(args, ["name"])
        print_json(add_team_member(args.db, args))
        return
    if args.command == "add-contact":
        require_args(args, ["name"])
        print_json(add_contact(args.db, args))
        return
    if args.command == "add-task":
        require_args(args, ["title"])
        print_json(add_task(args.db, args))
        return
    if args.command == "list":
        print_json(list_table(args.db, args.table or "customers"))
        return
    if args.command in {"daily-brief", "brief"}:
        print_json(local_daily_brief(args.db))
        return
    if not check_license(args.db, args.command).get("allowed"):
        print_json(license_required(args.command))
        return
    response = run_cloud_core(args.command, args.db, args, export_data(args.db))
    print(response.get("output") or json.dumps(response, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
