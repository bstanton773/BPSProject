from app import app
from flask import render_template, redirect, flash, url_for, request

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
    if current_user.is_anonymous:
        return redirect(url_for('login'))
    product_in_cart = Cart.query.filter_by(user_id = current_user.id).join(
        Product, Cart.product_id == Product.product_id).add_columns(
        Product.name, Product.price, Product.image, Product.product_id).all()
    return render_template('cart.html', products=product_in_cart, totalPrice=300, loggedIn=current_user)

@app.route('/addToCart/<int:product_id>/<string:from_page>')
def addToCart(product_id, from_page):
    if current_user.is_anonymous:
        return redirect(url_for('login'))
    cart = Cart(user_id = current_user.id, product_id = product_id)
    db.session.add(cart)
    db.session.commit()
    return redirect(url_for('cart'))

@app.route('/removeFromCart/<int:product_id>/<string:from_page>')
def removeFromCart(product_id, from_page):
    if current_user.is_anonymous:
        return redirect(url_for('login'))
    cart = Cart.query.filter_by(user_id=current_user.id, product_id=product_id).first()
    db.session.delete(cart)
    db.session.commit()
    if from_page == 'checkout':
        return redirect(url_for('checkout'))
    else:
        return redirect(url_for('cart'))

@app.route('/product/<int:product_id>')
def details(product_id):
    product = Product.query.filter_by(product_id=product_id).first()
    return render_template('details.html', product=product)

@app.route('/checkout')
def checkout():
    if current_user.is_anonymous:
        return redirect(url_for('login'))
    product_in_cart = Cart.query.filter_by(user_id = current_user.id).join(
        Product, Cart.product_id == Product.product_id).add_columns(
        Product.name, Product.price, Product.image, Product.product_id).all()
    #count
    count = Cart.query.filter_by(user_id = current_user.id).count()
    #subtotal
    sum = 0
    for product in product_in_cart:
        sum += product.price
    return render_template('checkout.html', products=product_in_cart, count=count, sub_total=sum)

@app.route("/checkout_action", methods=['POST'])
def checkout_action():

   # get submit bill info
   cardname = request.form.get('cardname')
   cardnumber = request.form.get('cardnumber')


   # gather selected checkout items
   product_in_cart = Cart.query.filter_by(user_id = current_user.id).join(
       Product, Cart.product_id == Product.product_id).add_columns(
       Product.name, Product.price, Product.image, Product.product_id).all()

   # create a checkout submit record and put it to the db



   # remove selected checkout items

   print("checkout_action:" + cardname + cardnumber)
   return render_template("checkout_action.html")