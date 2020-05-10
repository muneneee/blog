from flask import render_template,request,redirect,url_for,abort
from app.requests import get_quotes
from . import main
from .forms import BlogForm,CommentForm
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



@main.route('/blog', methods = ['GET','POST'])
@login_required
def new_blog():
    form = BlogForm()

    if form.validate_on_submit():
        blog_title = form.title.data
        blog = form.pitch.data
        new_blog = Blog(blog_title=blog_title,blog = blog)
        new_pitch.save_blog()
        return redirect(url_for('main.index'))


    title = 'New Blog'
    return render_template('blog.html' ,title = title, blog_form = form)


