# Importing libraries
from flask import Flask,request,make_response,render_template,jsonify
import requests
import logging
import sys

# Initializing flask app
app = Flask(__name__)

# Task 1
@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')

#Task 2
@app.route('/authors',methods=['GET'])
def authors():
    data = requests.get('https://jsonplaceholder.typicode.com/users').json()
    posts = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    users = {d['id']:{'name':d['name'],'count':0} for d in data}
    for post in posts:
        users[post['userId']]['count']+=1
    return render_template('authors.html',users=users)

# Task 3
@app.route('/cookieform',methods=['POST','GET'])
def cookie():
    return render_template('cookie_form.html')

#Task 3
@app.route('/setcookie',methods=['GET','POST'])
def setcookie():
    name = request.form.get('name')
    age = request.form.get('age')
    resp = make_response("Created cookie ! go to <a href='/getcookie'>/getcookie</a> to see the cookie!")
    #resp.set_cookie('Cookie',{"name":"Akshay","age":20})
    resp.set_cookie("Name",name)
    resp.set_cookie("Age",age)
    return resp

# Task 4
@app.route('/getcookie',methods=['GET'])
def getcookie():
    name = request.cookies.get("Name")
    age = request.cookies.get("Age")
    return "Name : {} <br> Age : {} ".format(name,age)

# Task 5
@app.route('/robots.txt',methods=['GET'])
def deny():
    return render_template('robots.html')

# Task 6
@app.route('/html',methods=['GET'])
def html():
    return render_template('hello.html')

# Task 7
@app.route('/input',methods=['POST','GET'])
def input_request():
    return render_template('input.html')

# Task 7
@app.route('/output',methods=['POST'])
def output_request():
    data = request.form.get('text')
    app.logger.debug(data)
    return render_template('output.html',text=data)

if __name__ == '__main__':
    app.logger.addHandler(logging.StreamHandler(sys.stdout))
    app.logger.addHandler(logging.FileHandler('app_logs.log'))
    app.logger.setLevel(logging.DEBUG)
    app.run(port=8080,debug=True)
