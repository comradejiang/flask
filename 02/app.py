from flask import Flask, render_template,request
from utils import save_user_to_json, save_to_json

app = Flask(__name__)


@app.route("/login", methods=["GET"])
def login():
    return render_template("login.html")


@app.route("/register", methods=["GET"])
def register():
    return render_template("register.html")


@app.route("/login2", methods=["POST"])
def login2():
    return "success"


@app.route("/register2", methods=["POST"])
def register2():
    username = request.form.get("username")
    password = request.form.get("password")
    repeat_password = request.form.get("repeat_password")
    print(username,password,repeat_password)
    if password == repeat_password:
        save_user_to_json({"username":username,"password":password})
        return {"success":0}
    else:
        return "密码不一致"


if __name__ == '__main__':
    app.run()
