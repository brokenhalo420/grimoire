from apscheduler.schedulers.background import BackgroundScheduler
from services.api_service import get_top_anime
from models import Anime

def update():
    for i in range(0,10000,500):
        anime_list = get_top_anime(i)
        for anime in anime_list:
            Anime.objects.update_or_create(
                title = f'{anime.title}',
                anime_id = anime.anime_id,
                rating = anime.rating,
                image_url = f'{anime.image_url}',
                defaults={
                    'anime_id': anime.anime_id,
                    'title': anime.title,
                    'rating': anime.rating,
                    'image_url': anime.image_url
                }
            )


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(update, 'interval', seconds = 60 * 60)
    scheduler.start()
