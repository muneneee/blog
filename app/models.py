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
    category = db.Column(db.String)
    blog_title = db.Column(db.String)
    blog = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    author = db.Column(db.Integer,db.ForeignKey("users.id"))

    comments = db.relationship('Comment', backref = 'blog', lazy ='dynamic')


    def save_blog(self):
        db.session.add(self)
        db.session.commit()

    
    @classmethod
    def get_blogs(cls):
        blogs = Blog.query.filter_by().all()
        return blogs

    @classmethod
    def get_all_blogs(cls):
        blogs = Blog.query.order_by('-id').all()
        return blogs


    def __repr__(self):
        return f'Blog {self.blog_title}'



class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    comment =  db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id'))
    posted = db.Column(db.DateTime,default=datetime.utcnow)


    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    
    @classmethod
    def get_comments(cls):
        comments= Comment.query.filter_by(blog_id=id).all()
        return comments