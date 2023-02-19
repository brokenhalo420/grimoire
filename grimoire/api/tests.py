from django.test import TestCase
from api import api_service
# Create your tests here.

class ApiServiceTestCase(TestCase):

    def test_api_service_returns_top_first_anime(self):
        anime = api_service.get_top_anime(0,1)
        self.assertTrue('data' in anime)
    
    def test_api_service_get_anime_by_title(self):
        anime = api_service.get_anime_by_title('Fullmetal Alchemist: Brotherhood')
        self.assertTrue('node' in anime[0])