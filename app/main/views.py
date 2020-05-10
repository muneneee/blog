from flask import render_template,request,redirect,url_for,abort
from app.requests import get_quotes
from . import main
from .forms import UpdateProfile,PitchForm,CommentForm
from flask_login import login_required, current_user
from .. import db
from ..models import User,Blog,Comment



@main.route('/')
def index():


    blogs = Blog.get_blogs()


    title = 'K Blog'
    return render_template('index.html',title = title, comments = comments)



@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    title = f'{uname} profile'


    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user, title = title)


