from flask import Flask, flash, render_template, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask('my_app')
app.config['SECRET_KEY'] = 'my_top_secret_key'

db = SQLAlchemy(app)

import views

if __name__ == "__main__":
    app.run()
