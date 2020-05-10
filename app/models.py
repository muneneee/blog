from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



class Quote:

    def __init__(self,author,quote):
        self.author = author
        self.quote = quote



class User(db.Model,UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    profile_pic_path = db.Column(db.String())
    bio = db.Column(db.String(255))
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    pass_secure = db.Column(db.String(255))


    blog = db.relationship('Blog',backref = 'user' , lazy = "dynamic")
    comments = db.relationship('Comment', backref = 'user', lazy ='dynamic')


    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)


    def __repr__(self):
        return f'User {self.username}'



class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy = "dynamic")

    def __repr__(self):
        return f'User {self.name}'



class Blog(db.Model):

    __tablename__ = 'blogs'

    id = db.Column(db.Integer,primary_key = True)
    pitch_id = db.Column(db.Integer)
    category = db.Column(db.String)
    blog_title = db.Column(db.String)
    blog = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    author = db.Column(db.Integer,db.ForeignKey("users.id"))

    comments = db.relationship('Comment', backref = 'pitch', lazy ='dynamic')