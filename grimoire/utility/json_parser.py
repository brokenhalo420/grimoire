import json
from repository.models import Anime


def parse_json_to_anime(json_dictionary):
    try:
        anime = Anime()
        if 'id' in json_dictionary:
            anime.anime_id = json_dictionary['id']
        else:
            return None
        
        if 'title' in json_dictionary:
            anime.title = json_dictionary['title']
        else:
            return None

        if 'main_picture' in json_dictionary:
            if 'large' in json_dictionary['main_picture']:
                anime.image_url = json_dictionary['main_picture']['large']
            elif 'medium' in json_dictionary['main_picture']:
                anime.image_url = json_dictionary['main_picture']['medium']
            else :
                anime.image_url = ''
        else:
            anime.image_url = ''

        if 'mean' in json_dictionary:
            anime.rating = json_dictionary['mean']
        else:
            anime.rating = 0
        
        if 'synopsis' in json_dictionary:
            anime.description = json_dictionary['synopsis']
        else:
            anime.description = ''

        return anime
    except Exception:
        print(json_dictionary)
        return None

def parse_json_response_to_anime_list(json_response):
    if 'data' not in json_response:
        print(json_response)
        return []
    

    json_response = json_response['data']
    json_response = list(map(lambda x: x['node'], json_response))
    anime_list = list(map(lambda x: parse_json_to_anime(x), json_response))
    return anime_list
