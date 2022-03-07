import requests
import json
from django.test import TestCase
from rest_framework.test import APIRequestFactory
from .digikala_api.api import ScrapingApiView


    
class TestProject(TestCase):
    
    def setUp(self ):
        self.factory = APIRequestFactory()
        self.view = ScrapingApiView.as_view()
        self.url = "https://www.digikala.com/search/category-car-stereo/"
        
    def test_url(self) :
            
        web_page = requests.get(self.url)

        
        return self.assertEqual(web_page.status_code , 200)
    
    def test_api(self):
        request = self.factory.post(self.view , {"url" : self.url} )
        response = self.view(request , pk=1)
        response.render()

        key = ["name" , "price" , "exist" , "color" , "rate" , "saler" , "discription" , "gurantee"]
        
        
        response = list (json.loads(response.content.decode("utf-8")).keys())
        

        self.assertEqual(response , key)
        
