#-*- coding:utf-8 -*-

from flask import Flask,jsonify,url_for,render_template,redirect,Response
from flask import request
from datetime import datetime


app = Flask(__name__, static_folder='CreateOrder/static',template_folder='CreateOrder/templates')

@app.route('/', methods=['GET', 'POST'])
def home():
    return '''<h1><font color="DarkBlue ">维信卡卡贷造单工具</font></h1>
              <h2>author:Robert<h2>
           '''

@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''

@app.route('/signin', methods=['POST'])
def signin():
    # 需要从request对象读取表单内容：
    if request.form['username']=='admin' and request.form['password']=='password':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'

@app.route('/page',methods=['GET'])
def page():
    # return url_for('CreateOrder\static',filename='style.css')
    return "test static page!!"

@app.route('/page/showpicture')
def showpicture():
    __tempurl=url_for('static', filename='img/vacationflog.jpg', _external=True)
    respon = Response(__tempurl,mimetype='image/jgeg')
    return respon

@app.route('/page/showhtml',methods=['GET'])
def showhtml():
    __tempurl = url_for("static",filename="css/style.css")
    print(__tempurl)
    temp_datetime=datetime.now().strftime("%b %d %Y %H:%M:%S")
    return render_template("user.html",name='Robert',datetime=temp_datetime)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)