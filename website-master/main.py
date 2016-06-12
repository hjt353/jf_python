#coding:utf8

from flask import Flask,render_template,request,url_for,redirect
from modules import conf,user

app = Flask(__name__)

@app.route("/")
def index():
    return "welcome to home."

@app.route("/login",methods=['GET','POST'])
def login():
    if request.method == 'POST':
        phone = request.form["phone"]
        password = request.form["password"]
        user_auth = user.User()
        result = user_auth.user_login(phone=phone,password=password)
        if result["code"] == 0:#rewrite index html
            return redirect("/")
        else:#rewrite error html
            return str(result["message"])
    return render_template("login.html")

@app.route("/reg",methods=['GET','POST'])
def register():
    if request.method == 'POST':
        phone = request.form["phone"]
        password = request.form["password"]
        username = request.form["username"]
        ensure_password = request.form["ensure_password"]
        stage_class = request.form["stage_class"]
        user_reg = user.User()
        result = user_reg.user_reg(phone=phone,
                                 username=username,
                                 password=password,
                                 ensure_password=ensure_password,
                                 stage_class=stage_class)
        if result["code"] == 0:
            return redirect("/")
        else:
            return str(result["message"])
    return render_template("register.html")


@app.route("/admin",methods=['GET','POST'])
def admin():
    #假设已经登录成功 并获取用户 id
    if request.method == 'POST':


    return render_template("admin.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=80,debug=True)
