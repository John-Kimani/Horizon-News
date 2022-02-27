from app import app
import urllib.request,json
from .models import Source

news = Source


def get_source(category):
    '''
    Function that get json to url request

    defines url apikey properties
    '''
    news_source_url = app.config['NEWS_SOURCE_URL']
    apiKey = app.config['NEWS_APIKEY']
    get_source_url = news_source_url.format(category, apiKey)

    '''
    Context manager that sends request 
    '''
    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)

        source_results = None

        if get_source_response['sources']:
            source_results_list = get_source_response['sources']
            source_results = process_results(source_results_list)

    return source_results