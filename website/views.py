from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    # pass
    # return "<h1>Testing</h1>"
    return render_template("home.html")

@views.route('/login')
def login():
    # pass
    # return "<h1>Testing</h1>"
    return render_template("login.html")
@views.route('/sign-up')
def sign_up():
    # pass
    # return "<h1>Testing</h1>"
    return render_template("sign_up.html")