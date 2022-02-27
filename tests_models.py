import unittest
from app.models import Source
news_source = Source


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


if __name__ == '__main__':
    unittest.main()

