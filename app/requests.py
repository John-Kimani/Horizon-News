from app import app,models
import urllib.request,json


news = models.Source
article_body = models.Article


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


def process_results(source_list):
    '''
    Function that process source results and transform them to a list of objects
    
    Args:
        source_list: Dictionaries that contain source details
        
    Returns:
        source_results: List on new objects
    '''
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        country = source_item.get('country')
        if description:
            source_object = news(id, name, description, url, category,country)
            source_results.append(source_object)

    return source_results


#articles starts

def get_articles(source_id):
    '''
    Function to get articles
    '''
    article_source_url = app.config['NEWS_ARTICLE_URL']
    apiKey = app.config['NEWS_APIKEY']
    get_articles_url = article_source_url.format(source_id , apiKey)

    '''
    Context manager that sends article request
    '''
    with urllib.request.urlopen(get_articles_url) as url:
        get_article_data = url.read()
        get_article_response = json.loads(get_article_data)


        articles_results = None

        if get_article_response['articles']:
            articles_results_list = get_article_response['articles']
            articles_results = process_articles(articles_results_list)

        return articles_results

def process_articles(articles_list):
    '''
    Function that process articles results and transform them to list of objects
    Args:
        articles_list: Dictionary that contain articles 
    Returns:
        articles_results: List of new objects
    '''
    articles_results = []
    for article in articles_list:
        # source = article.get('source.id')
        author = article.get('author')
        title = article.get('title')
        description = article.get('description')
        url = article.get('url')
        urlToImage = article.get('urlToImage')
        publishedAt = article.get('publishedAt')
        content = article.get('content')
        if description:
            article_object = article_body( author, title, description, url, urlToImage, publishedAt, content)
            articles_results.append(article_object) 

        return articles_results
