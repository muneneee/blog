from flask import Flask
from app import app


@app.route('/')
def index():

    rettun render_template('index.html')