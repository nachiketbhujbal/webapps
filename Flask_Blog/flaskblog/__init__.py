from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationFrom, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'bc643a510f94191f5e01e52938fbb866'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)
