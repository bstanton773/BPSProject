from app import app
from flask import render_template, redirect, flash, url_for

from flask_login import current_user
from app.models import Post
from app import db


@app.route("/")
@app.route('/index')
def index():
    posts = Post.query.all()
    return render_template('index.html', title='The Title',user=current_user, posts=posts)


@app.route('/bitcoin')
def bitcoin():
    return render_template('bitcoin.html')