from app import app
from flask import render_template, redirect, flash, url_for

from flask_login import current_user
from app.models import Post, Product, Cart
from app import db


@app.route('/')
@app.route('/index')
def index():
    posts = Post.query.all()
    return render_template('index.html', title='The Title',user=current_user, posts=posts)


@app.route('/bitcoin')
def bitcoin():
    return render_template('bitcoin.html')

@app.route('/store')
@app.route('/products')
def products():
    product_list = Product.query.all()
    return render_template('products.html', products = product_list)


@app.route('/cart')
def cart():
    cart_list = Cart.query.all()
    return render_template('cart.html', carts = cart_list)

@app.route('/addToCart/<int:product_id>/<string:from_page>')
def addToCart(product_id, from_page):
    if current_user.is_anonymous:
        return redirect(url_for('login'))
    cart = Cart(user_id = current_user.id, product_id = product_id)
    db.session.add(cart)
    db.session.commit()
    return redirect(url_for('cart'))

