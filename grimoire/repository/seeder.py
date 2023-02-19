from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from utility import json_parser
from api import api_service
from .models import Anime
import time


DB_MAXIMUM_MODELS = 10000
# ANIME PER REQUEST - MAXIMUM 500
STEP = 500


def update():
    range_list = getRange()
    limit = STEP
    rest = Anime.objects.count() - (Anime.objects.count() // STEP)
    if rest < STEP and rest != 0:
        limit = rest

    for i in range_list:
        anime_list = json_parser.parse_json_response_to_anime_list(
            api_service.get_top_anime(limit=limit, offset=i))
        for anime in anime_list:
            if anime is None:
                continue

            anime_in_db, created = Anime.objects.get_or_create(
                title=f'{anime.title}',
                defaults={
                    'anime_id': anime.anime_id,
                    'title': anime.title,
                    'rating': anime.rating,
                    'image_url': anime.image_url,
                    'description': anime.description
                }
            )

            if not created:
                anime_in_db.anime_id = anime.anime_id
                anime_in_db.title = anime.title
                anime_in_db.rating = anime.rating
                anime_in_db.image_url = anime.image_url
                anime_in_db.description = anime.description
                anime_in_db.save()

    print(f'{datetime.now()}: Done!')


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(update, 'interval', hours=1,
                      next_run_time=datetime.now())
    scheduler.start()

    try:
        time.sleep(2)
    except( KeyboardInterrupt, SystemExit):
        scheduler.shutdown()


def getRange():
    print(f'objects count: {Anime.objects.count()}')
    if Anime.objects.count() == 0 or Anime.objects.count() <= DB_MAXIMUM_MODELS:
        return list(range(0, DB_MAXIMUM_MODELS, STEP))
    else:
        max = (Anime.objects.count() // STEP) * STEP
        range_list = list(range(0, max, STEP))
        if (Anime.objects.count() - max != 0):
            range_list.append(max)
        return range_list
