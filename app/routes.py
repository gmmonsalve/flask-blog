from flask import render_template
from app import app

@app.route('/')
def index():
    user = {'username': 'Gabriela'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html',title='Welcome',posts=posts,user=user) 