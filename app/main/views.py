from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from .forms import BlogForm,CommentForm
from flask_login import login_required, current_user
from .. import db
from ..models import User,Post,Comment



@main.route('/')
def index():

    

    posts = Post.query.all()

    
    title = 'K Blog'
    return render_template('index.html',title = title,posts =posts)



@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    title = f'{uname} profile'


    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user, title = title)




@main.route('/blog', methods = ['GET','POST'])
@login_required
def new_post():
    blog_form = BlogForm()

    if blog_form.validate_on_submit():
        post = Post(title=blog_form.title.data, content=blog_form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('main.index'))


    title = 'New Blog'
    return render_template('blog.html' ,title = title, blog_form = blog_form)



@main.route('/blog/<int:post_id>/comment', methods = ['GET','POST'])
@login_required
def comment(post_id):
    comment_form = CommentForm()
    my_blog = Post.query.get(post_id)

    if my_blog is None:
        abort(404)
    

    if comment_form.validate_on_submit():
        comment = comment_form.comment.data
        new_comment = Comment(comment = comment, post_id = post_id, user = current_user)
        new_comment.save_comment()
        return redirect(url_for('main.comment', post_id=post_id))

    all_comments = Comment.query.filter_by(post_id=post_id).all()

    title = 'comment'
    return render_template('comment.html' ,title = title, comment_form = comment_form, comment=all_comments)


@main.route('/blog/<int:post_id>/update', methods =['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get(post_id)
    if post.author != current_user:
        abort(403)
    blog_form = BlogForm()
    if blog_form.validate_on_submit():
        post.title = blog_form.title.data
        post.content = blog_form.content.data
        db.session.commit()
        flash('Your blog has been updated!', 'success')
        return redirect(url_for('main.index', post_id=post.id))
    elif request.method == 'GET':
        blog_form.title.data = post.title
        blog_form.content.data = post.content
    return render_template('blog.html',title = 'Update post', blog_form=blog_form)


@main.route('/blog/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get(post_id)
    if post.author == current_user:
        db.session.delete(post)
        db.session.commit()
        flash('Your post has been deleted!', 'success')
        return redirect(url_for('main.index'))




    