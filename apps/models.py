from wtforms.validators import Length
from apps import db, login_manager
from apps import bcrypt
from flask_login import UserMixin
from sqlalchemy.sql import func

#used for logging in users
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#USER TABLE
class User(db.Model, UserMixin):
    #consider changing id to user_id
    id = db.Column(db.Integer(), primary_key = True)
    username = db.Column(db.String(length = 30), nullable = False, unique = True)
    fullname = db.Column(db.String(length = 30), nullable = False)
    address = db.Column(db.String(length = 50), nullable = False)
    phone_number = db.Column(db.Integer(), nullable = False)
    password_hash = db.Column(db.String(length = 60), nullable = False)

    tables = db.relationship('Table', backref = 'reserved_user', lazy = True) # relationship with 'Table'
    items = db.relationship('Item', backref = 'ordered_user', lazy = True) # relationship with 'Item'
    orders = db.relationship('Order', backref = 'order-id_user', lazy = True) #relationship with 'Table')

    @property
    def password(self):
        return self.password
    
    #hashes the user's password
    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    #verifies if the entered password in sign in form matches the user's password in the database
    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)
        
#TABLE RESERVATION TABLE
class Table(db.Model):
    #consider changing id to table_id
    table_id = db.Column(db.Integer(), primary_key = True)
    table = db.Column(db.Integer(), nullable = False)
    time = db.Column(db.String(length = 20), nullable = False)
    date = db.Column(db.String(length = 20), nullable = False)
    accomodation = db.Column(db.Integer(), nullable = False)
    #suggestion: you might want to change 'owner' to 'reservee'
    reservee = db.Column(db.String(), db.ForeignKey('user.id'))  #used to store info regarding user's reserved table

    #function for assigning ownership to the user's reserved table
    def assign_ownership(self, user):
        self.reservee = user.fullname 
        db.session.commit()
    def remove_ownership(self, user):
        self.orderer = None
        db.session.commit()

#MENU TABLE
class Item(db.Model):
    #consider changing id to item_id
    item_id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(length = 30), nullable = False)
    description = db.Column(db.String(length = 50), nullable = False)
    price = db.Column(db.Integer(), nullable = False)
    source = db.Column(db.String(length = 30), nullable = False)
    #suggestion: you might want to change 'owner' to 'orderer'/ 'customer'
    orderer = db.Column(db.Integer(), db.ForeignKey('user.id'))  #used to store info regarding user's ordered item
    
    def __init__(self, name, description, price, source):
        self.name = name
        self.description = description
        self.price = price
        self.source = source
        
    #function for assigning ownership to the user's selected item
    def assign_ownership(self, user):
        self.orderer = user.id 
        db.session.commit()

    def remove_ownership(self, user):
        self.orderer = None
        db.session.commit()

# Define Order model
class Order(db.Model):
    order_id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'), nullable=False)
    address = db.Column(db.String(length=50), nullable=False)
    datetime = db.Column(db.DateTime(timezone=True), server_default=func.now())
    
    
    def __init__(self, user_id, address):
        self.user_id = user_id
        self.address = address

# Define Cart model
class CartItem(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'), nullable=False)
    item_id = db.Column(db.Integer(), db.ForeignKey('item.item_id'), nullable=False)
    quantity = db.Column(db.Integer(), nullable=False, default=1)
    
    
  



