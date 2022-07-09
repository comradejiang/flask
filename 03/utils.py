import json
import os.path



#保存数据
def save_user_to_json(user_info):
    user_list = load_users()
    user_list.append(user_info)

    with open("./users.json", "w") as f:
        f.write(json.dumps(user_list, ensure_ascii=False, indent=2))

#加载数据
def load_users():
    if os.path.exists("./users.json"):
        return json.loads(open("./users.json").read())
    else:
        return []

#验证数据
def user_password_exist(username, password):
    exist = False
    for user_info in load_users():
        if user_info["username"] == username and user_info["password"] == password:
            exist = True
            break
    return exist
