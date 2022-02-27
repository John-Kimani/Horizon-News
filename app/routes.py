from flask import render_template
from app import app
from .requests import get_source


@app.route('/')
@app.route('/index')
def index():
    '''
    View function that returns index page and data
    '''
    news_sources = get_source('general')
    print(news_sources)
    return render_template('index.html',title='Home', news_sources=news_sources)


@app.route('/articles')
def articles():
    return render_template('articles.html', title='Articles')