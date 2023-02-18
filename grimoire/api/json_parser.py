import json
from .models import Anime


def parse_json_to_anime(json_dictionary):
    anime = Anime()
    anime.anime_id = json_dictionary['id']
    anime.title = json_dictionary['title']
    anime.image_url = json_dictionary['main_picture']['large']
    anime.rating = json_dictionary['mean']

    return anime

def parse_json_response_to_anime_list(json_response):
    json_response = json_response['data']
    json_response = list(map(lambda x: x['node'], json_response))

    anime_list = list(map(lambda x: parse_json_to_anime(x), json_response))
    return anime_list