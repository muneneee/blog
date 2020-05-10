from flask import render_template
from . import main


@main.route('/')
def index():


    title = 'Kevin Blog'
    return render_template('index.html',title = title)