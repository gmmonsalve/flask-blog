from flask import render_template, redirect, flash, url_for, request
from app import app
from app.forms import LoginForm
from app.models import User, Post
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

@app.route('/')
def index():
    return redirect(url_for('login'))
''' this is only for test'''
@app.route('/home')
@login_required
def home():
    posts = [
        {
            'author': {'username': 'gmmonsalve'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'gmmonsalve'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('home.html', title="Home page", posts=posts)

@app.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid usename or password')
            return redirect(url_for('login'))
        login_user(user,remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('home')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register')
def register():
    return render_template('login.html')