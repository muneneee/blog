from flask import render_template,request,redirect,url_for,abort
from . import main
from .forms import BlogForm,CommentForm
from flask_login import login_required, current_user
from .. import db
from ..models import User,Blog,Comment



@main.route('/')
def index():

    

    blogs = Blog.query.all()

    
    title = 'K Blog'
    return render_template('index.html',title = title,blogs =blogs)



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
        blog = form.blog.data
        new_blog = Blog(blog_title=blog_title,blog = blog)
        new_blog.save_blog()
        return redirect(url_for('main.index'))


    title = 'New Blog'
    return render_template('blog.html' ,title = title, blog_form = form)



@main.route('/blog/<int:blog_id>/comment', methods = ['GET','POST'])
@login_required
def comment(blog_id):
    comment_form = CommentForm()
    my_blog = Blog.query.get(blog_id)

    if my_blog is None:
        abort(404)
    

    if comment_form.validate_on_submit():
        comment = comment_form.comment.data
        new_comment = Comment(comment = comment, blog_id = blog_id, user = current_user)
        new_comment.save_comment()
        return redirect(url_for('.comment', blog_id=blog_id))

    all_comments = Comment.query.filter_by(blog_id=blog_id).all()

    title = 'comment'
    return render_template('comment.html' ,title = title, comment_form = comment_form, comment=all_comments)


@main.route('/blog/<int:blog_id>/update', methods =['GET', 'POST'])
@login_required
def update_blog(blog_id):
    blog = Blog.query.get(blog_id)
    if blog.author != current_user:
        abort(403)
    form = BlogForm()
    if form.validate_on_submit():
        blog.title = form.title.data
        blog.blog = form.content.data
        db.session.commit()
        flash('Your blog has been updated!', 'success')
        return redirect(url_for('blog', blog_id=blog.id))
    elif request.method == 'GET':
        form.title.data = blog.title
        form.blog.data = blog.blog
    return render_template('blog.html',title = 'Update post', form=form)


@main.route('/blog/<int:blog_id>/delete', methods=['POST'])
@login_required
def delete_blog(blog_id):
    blog = Blog.query.get(blog_id)
    if blog.author != current_user:
        abort(403)
    db.session.delete(blog)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('main.index'))




    