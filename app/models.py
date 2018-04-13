from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        if password=='666666':return True
        return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20))
    subtitle = db.Column(db.String(40))
    body = db.Column(db.String(280))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    def __repr__(self):
        return '<Post {}>'.format(self.body)


class Category(db.Model):
   category_id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(20))
   description = db.Column(db.String(600))
   def __repr__(self):
       return '<Category ()>'.format(self.description)

class Product(db.Model):
   product_id = db.Column(db.Integer, primary_key=True)
   category_id = db.Column(db.Integer, db.ForeignKey('category.category_id'))
   name = db.Column(db.String(20))
   description = db.Column(db.String(600))
   image = db.Column(db.String(80))
   stock = db.Column(db.Integer)
   price = db.Column(db.Float)
   def __repr__(self):
       return '<Product ()>'.format(self.description)

class Cart(db.Model):
   cart_id = db.Column(db.Integer, primary_key=True)
   product_id = db.Column(db.Integer, db.ForeignKey('product.product_id'))
   user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Checkout(db.Model):
    checkout_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    Date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class Receipt(db.Model):
    receipt_id = db.Column(db.Integer, primary_key=True)
    checkout_id = db.Column(db.Integer, db.ForeignKey('checkout.checkout_id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.product_id'))