from django.test import TestCase
import requests

class TestBlogApi(TestCase):
    def test_get_posts(self):
        url = 'http://127.0.0.1:8000'
        request = requests.get(url)
        self.assertEqual(request.status_code, 200)
        # {'message': 'Welcome to the blog API!'}
        self.assertEqual(request.json(), {'message': 'Welcome to the blog API!'})
        
    request = requests.get('http://127.0.0.1:8000')
    print(request.json())
        
    

# Create your tests here.
