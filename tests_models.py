import unittest
from app.models import Source,Article
news_source = Source
news_article = Article

class Test_Source(unittest.TestCase):
    '''
    Test class to test behavior of sources class
    '''
    def setup(self):
        '''
        Set up method that runs before each test
        '''
        self.news_source = Source(1997, 'KimNews', 'Created by Kim', 'http://kimperria.com', 'technology', 'Kenya')

    def test_init(self):
        '''
        Test to check if new object it properly initialized
        '''
        self.assertEqual(self.news_source.id, 1997)
        self.assertEqual(self.news_source.name, 'KimNews')
        self.assertEqual(self.news_source.description, 'Created by Kim')
        self.assertEqual(self.news_source.url, 'http://kimperria.com')
        self.assertEqual(self.news_source.category, 'technology')
        self.assertEqual(self.news_source.country, 'Kenya')


class Test_Article(unittest.TestCase):
    '''
    Test class to test behaviour of articles class
    '''
    def setUp(self):
        '''
        Set up method that runs before each test
        '''
        self.news_article = Article('BBC', 'Kimperria','Fintech', 'All about fintech', 'https:/kimperia.com', 'https:/kimperria.com/images', '27/02/2021', 'Great news')



    def test__init(self):
        '''
        Test to check if new object is properly initialized
        '''
        self.news_article = Article()
        self.assertEqual(self.news_article.source)
        self.assertEqual(self.news_article.author)
        self.assertEqual(self.news_article.title)
        self.assertEqual(self.news_article.description)
        self.assertEqual(self.news_article.url)
        self.assertEqual(self.news_article.urlToImage)
        self.assertEqual(self.news_article.publishedAt)
        self.assertEqual(self.news_article.content)

if __name__ == '__main__':
    unittest.main()

