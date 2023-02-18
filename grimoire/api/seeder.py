from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from . import json_parser
from . import api_service
from .models import Anime

DB_MAXIMUM_MODELS = 10000
#ANIME PER REQUEST - MAXIMUM 500
STEP = 500

def update():
    range_list = getRange()
    limit = STEP
    rest = Anime.objects.count() - (Anime.objects.count() // STEP)
    if rest < STEP:
        limit = rest
                    
    for i in range_list:
        anime_list = json_parser.parse_json_response_to_anime_list(api_service.get_top_anime(limit = limit, offset = i))
        for anime in anime_list:
            if anime is None:
                continue
            
            Anime.objects.update_or_create(
                title = f'{anime.title}',
                anime_id = anime.anime_id,
                rating = anime.rating,
                image_url = f'{anime.image_url}',
                description = f'{anime.description}',
                defaults={
                    'anime_id': anime.anime_id,
                    'title': anime.title,
                    'rating': anime.rating,
                    'image_url': anime.image_url,
                    'description': anime.description
                }
            )
    print(f'{datetime.now()}: Done!')


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(update, 'interval', hours = 1, next_run_time = datetime.now())
    scheduler.start()

def getRange():
    if Anime.objects.count() == 0:
        return list(range(0,DB_MAXIMUM_MODELS + 1, STEP))
    else:
        max = Anime.objects.count() // STEP
        range_list = list(range(0,max + 1,STEP))
        range_list.append(Anime.objects.count())
        return range_list