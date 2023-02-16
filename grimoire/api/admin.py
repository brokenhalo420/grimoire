from django.contrib import admin
from .models import User, Anime, SavedAnime

# Register your models here.
admin.site.register(User)
admin.site.register(Anime)
admin.site.register(SavedAnime)
