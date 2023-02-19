from django.db import models
from django.contrib.auth.models import User

# Create your models here.

CATEGORIES = [
    ('FAVORITE', 'Favorite'),
    ('WATCHLATER', 'Watch Later'),
    ('WATCHED', 'Watched'),
    ('NONE','None')
]

class Anime(models.Model):
    anime_id = models.IntegerField(default=0)
    title = models.CharField(max_length=200)
    rating = models.FloatField()
    image_url = models.TextField(max_length=500, default='')
    description = models.TextField(max_length=5000, default='')

    def __str__(self):
        return self.title

class SavedAnime(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    type = models.CharField(
        max_length = 20,
        choices = CATEGORIES,
        default = 'NONE'
    )

    def __str__(self) -> str:
        return f'{self.user.username} - {self.anime.title}'