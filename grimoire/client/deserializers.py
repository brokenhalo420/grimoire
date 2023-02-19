from api.models import Anime

def deserialize_anime(anime_dict):
    try:
        anime = Anime()
        if 'anime_id' in anime_dict:
            anime.anime_id = anime_dict['anime_id']
        else:
            return None
        
        if 'title' in anime_dict:
            anime.title = anime_dict['title']
        else:
            return None

        if 'image_url' in anime_dict:
            anime.image_url = anime_dict['image_url']
        else:
            anime.image_url = ''

        if 'rating' in anime_dict:
            anime.rating = anime_dict['rating']
        else:
            anime.rating = 0
        
        if 'description' in anime_dict:
            anime.description = anime_dict['description']
        else:
            anime.description = ''

        return anime
    except Exception:
        print(anime_dict)
        return None
    
def parse_anime_list(anime_list_json): 
    anime_list = list(map(lambda x: deserialize_anime(x), anime_list_json))
    return anime_list