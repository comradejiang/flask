from flask import Flask, render_template, request, session, redirect
from utils import save_user_to_json,  user_password_exist

app = Flask(__name__)
app.secret_key = "pioneer123"

#首页：未登录无法进入
@app.route("/", methods=["GET", "POST"])
def index():
    username = session.get("username")
    if not username:
        return redirect("/login")
    return render_template("index.html")

#登录页面：用于提交username和password
@app.route("/login", methods=["GET"])
def login():
    return render_template("login.html")

#注册页面：用于提交username和password并保存在json文件中
@app.route("/register", methods=["GET"])
def register():
    return render_template("register.html")

#用于验证u登录用户提交的sername和password是否存在于json文件中
@app.route("/login2", methods=["POST"])
def login2():
    username = request.form.get("username")
    password = request.form.get("password")
    if user_password_exist(username, password):
        session["username"] = username
        return {"success": 0}
    else:
        return {"success": 1}

#将用户提交的username和password保存在json中
@app.route("/register2", methods=["POST"])
def register2():
    username = request.form.get("username")
    password = request.form.get("password")
    repeat_password = request.form.get("repeat_password")
    print(username, password, repeat_password)
    if password == repeat_password:
        save_user_to_json({"username": username, "password": password})
        return {"success": 0}
    else:
        return "密码不一致"

#注销功能
@app.route("/logout",methods=["GET"])
def logout():
    session.pop("username")
    return {"success":0}




if __name__ == '__main__':
    app.run()
