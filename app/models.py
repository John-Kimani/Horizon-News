class Source:
    '''
    Class that defines news sources object
    '''


    def __init__(self, id, name, description, url, category, country):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.country = country


# top headlines

class Article:
    '''
    Class that defines article objects
    '''

    def __init__(self, source, author, title, description, url, urlToImage, publishedAt, content):
        self.source = source
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImahe = urlToImage
        self.publishedAt = publishedAt
        self.content = content
