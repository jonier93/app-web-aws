from flask import render_template, request
from server import app
from db import add_user

@app.route('/')
def func_home(): 
    add_user()
    return render_template("home.html")

@app.route('/register_page')
def func_register_page():
    return render_template("register.html")
    
@app.route("/consult_page")
def func_consult_page():
    return render_template("consult.html")

@app.route("/register_user", methods=["post"])
def func_register_user():
    data_user = request.form
    ident, name, lastname, birthday = data_user["id"], data_user["name"], data_user["lastname"], data_user["birthday"]
    print(ident, name, lastname, birthday)
    return "<h1> User was added </h1>"