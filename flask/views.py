from flask import flash, render_template, redirect

from app import app
from forms import LoginForm


@app.route("/login", methods=['GET', 'POST'])
def login():
    valid_credentials = {
        'username': 'user',
        'password': 'password',
    }
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if (login_form.username.data == valid_credentials['username']
                and login_form.password.data == valid_credentials['password']):
            return redirect('/')
        else:
            flash('Username or password are not valid')
    return render_template('login.html', form=login_form)


@app.route("/")
def hello():
    return "<h1>Hello World!</h1>"


@app.route("/index2")
def index2():
    return render_template('index2.html')


@app.route("/<name>")
def hello_name(name):
    # get 10 records from DB
    users = ['user1', 'user2', 'user3', 'user4']
    return render_template('index.html', username=name,
                           users=users)
