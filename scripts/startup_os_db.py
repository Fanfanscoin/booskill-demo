import argparse
import json
import sqlite3

from booskill_license import activate_license, check_license, run_cloud_core


SCHEMA = """
CREATE TABLE IF NOT EXISTS projects (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, created_at TEXT DEFAULT '', updated_at TEXT DEFAULT '');
CREATE TABLE IF NOT EXISTS team_members (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, role TEXT DEFAULT '', created_at TEXT DEFAULT '', updated_at TEXT DEFAULT '');
CREATE TABLE IF NOT EXISTS customers (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, owner TEXT DEFAULT '', status TEXT DEFAULT '', created_at TEXT DEFAULT '', updated_at TEXT DEFAULT '');
CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, owner TEXT DEFAULT '', due_date TEXT DEFAULT '', status TEXT DEFAULT 'todo', created_at TEXT DEFAULT '', updated_at TEXT DEFAULT '');
"""


def init_db(db):
    with sqlite3.connect(db) as conn:
        conn.executescript(SCHEMA)
        conn.commit()


def export_data(db):
    data = {}
    with sqlite3.connect(db) as conn:
        conn.row_factory = sqlite3.Row
        for table in ["projects", "team_members", "customers", "tasks"]:
            data[table] = [dict(row) for row in conn.execute(f"SELECT * FROM {table}").fetchall()]
    return data


def main():
    parser = argparse.ArgumentParser(description="BossSkill cloud client")
    parser.add_argument("command")
    parser.add_argument("--db", default="startup_os.sqlite3")
    parser.add_argument("--license-key")
    parser.add_argument("--text")
    args = parser.parse_args()
    init_db(args.db)
    if args.command == "init":
        print(f"initialized {args.db}")
        return
    if args.command == "activate-license":
        print(json.dumps(activate_license(args.db, args.license_key), ensure_ascii=False, indent=2))
        return
    if args.command == "license-status":
        print(json.dumps(check_license(args.db, "status"), ensure_ascii=False, indent=2))
        return
    response = run_cloud_core(args.command, args.db, args, export_data(args.db))
    print(response.get("output") or json.dumps(response, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
