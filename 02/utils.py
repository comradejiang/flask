import json
import os.path


def save_to_json(todo_items):
    with open("db.json", "w") as f:
        f.write(json.dumps(todo_items, ensure_ascii=False, indent=2))


def save_user_to_json(user_info):
    user_list = load_users()
    user_list.append(user_info)

    with open("./users.json", "w") as f:
        f.write(json.dumps(user_list, ensure_ascii=False, indent=2))


def load_users():
    if os.path.exists("./users.json"):
        return json.loads(open("./users.json").read())
    else:
        return []

