from django.contrib import admin
from .models import Anime, SavedAnime

# Register your models here.
admin.site.register(Anime)
admin.site.register(SavedAnime)
