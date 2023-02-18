from rest_framework import serializers
from .models import User, Anime, SavedAnime

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']


class AnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = ['anime_id', 'title', 'rating', 'image_url', 'description']


class SavedAnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedAnime
        fields = ['user', 'anime', 'type']
