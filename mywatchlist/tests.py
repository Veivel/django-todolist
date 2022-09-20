from django.test import TestCase

# Create your tests here.

class ViewsTestCase(TestCase):
    ''' Test case for HTML page. '''
    def test_index_loads_properly(self):
        response = self.client.get('/mywatchlist/html')
        self.assertEqual(response.status_code, 200)
        
class XMLTestCase(TestCase):
    ''' Test case for XML page. '''
    def test_index_loads_properly(self):
        response = self.client.get('/mywatchlist/xml')
        self.assertEqual(response.status_code, 200)
        
class JSONTestCase(TestCase):
    ''' Test case for JSON page. '''
    def test_index_loads_properly(self):
        response = self.client.get('/mywatchlist/json')
        self.assertEqual(response.status_code, 200)
        
        