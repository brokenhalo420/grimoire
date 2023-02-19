from django.test import TestCase
from utility import deserializers
# Create your tests here.

class AnimeDeserializerTestCase(TestCase):
    
    def anime_deserializer_should_return_anime_object(self):
        anime = {
            'anime_id': 1,
            'title': "TestTitle",
            'image_url': 'TestImageUrl',
            'rating': 3.14,
            'description': "Test description"
        }

        animeParsed = deserializers.deserialize_anime(anime)
        self.assertEquals(animeParsed.anime_id, anime['anime_id'])
        self.assertEquals(animeParsed.title, anime['title'])
        self.assertEquals(animeParsed.image_url, anime['image_url'])
        self.assertEquals(animeParsed.rating, anime['rating'])
        self.assertEquals(animeParsed.description, anime['description'])

    def anime_deserializer_should_return_none_on_missing_id(self):
        anime = {
            'title': "TestTitle",
            'image_url': 'TestImageUrl',
            'rating': 3.14,
            'description': "Test description"
        }

        animeParsed = deserializers.deserialize_anime(anime)
        self.assertTrue(animeParsed is None)

    
    def anime_deserializer_should_return_none_on_missing_title(self):
        anime = {
            'anime_id': 1,
            'image_url': 'TestImageUrl',
            'rating': 3.14,
            'description': "Test description"
        }

        animeParsed = deserializers.deserialize_anime(anime)
        self.assertTrue(animeParsed is None)
    
    def anime_deserializer_should_return_default_values_on_missing_image_description_rating(self):
        anime = {
            'anime_id': 1,
            'title': "TestTitle",
        }

        animeParsed = deserializers.deserialize_anime(anime)
        self.assertEquals(animeParsed.image_url, '')
        self.assertEquals(animeParsed.rating, 0)
        self.assertEquals(animeParsed.description, 0)


    def anime_deserialize_list_should_return_list_of_one_object(self):
        anime = [{
            'anime_id': 1,
            'title': "TestTitle",
            'image_url': 'TestImageUrl',
            'rating': 3.14,
            'description': "Test description"
        }]

        animeParsed = deserializers.parse_anime_list(anime)
        self.assertEquals(animeParsed[0].anime_id, anime[0]['anime_id'])
        self.assertEquals(animeParsed[0].title, anime[0]['title'])
        self.assertEquals(animeParsed[0].image_url, anime[0]['image_url'])
        self.assertEquals(animeParsed[0].rating, anime[0]['rating'])
        self.assertEquals(animeParsed[0].description, anime[0]['description'])