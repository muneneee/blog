from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required


class BlogForm(FlaskForm):

    
    title = StringField('Blog title',validators=[Required()])
    content = TextAreaField('Blog', validators=[Required()])
    submit = SubmitField('Submit')


class CommentForm(FlaskForm):
    comment = TextAreaField("Leave a comment", validators = [Required()])
    submit = SubmitField("Post")


class SubForm(FlaskForm):
    submit = SubmitField("Get notifications for every new blog")