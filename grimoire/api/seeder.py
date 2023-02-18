import datetime
from apscheduler.schedulers.background import BackgroundScheduler

from . import json_parser
from . import api_service
from .models import Anime

def update():
    for i in range(0,10000,100):
        anime_list = json_parser.parse_json_response_to_anime_list(api_service.get_top_anime(i))
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


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(update, 'interval', minutes = 30, next_run_time = datetime.datetime.now())
    scheduler.start()
