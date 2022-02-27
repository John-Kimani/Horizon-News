import os


class Config(object):
    '''
    Parent class configuration for horizon news web app
    '''
    NEWS_SOURCE_URL = os.environ.get('NEWS_SOURCE_URL')
    NEWS_ARTICLE_API_URL = os.environ.get('NEWS_ARTICLE_API_URL')
    NEWS_APIKEY = os.environ.get('NEWS_APIKEY')