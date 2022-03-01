import os


class Config(object):
    '''
    Parent class configuration for horizon news web app
    '''
    # NEWS_SOURCE_URL = os.environ.get('NEWS_SOURCE_URL')
    #test
    NEWS_SOURCE_URL='https://newsapi.org/v2/sources?category={}&apiKey={}'
    NEWS_ARTICLE_URL='https://newsapi.org/v2/everything?q={}&sortBy=popularity&apiKey={}'
    # NEWS_ARTICLE_URL = os.environ.get('NEWS_ARTICLE_URL')
    # NEWS_TOP_STORIES_API_URL = os.environ.get('NEWS_TOP_STORIES_API_URL')
    NEWS_APIKEY = os.environ.get('NEWS_APIKEY')

    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')