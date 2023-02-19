from rest_framework import serializers
from repository.models import Anime, SavedAnime


class AnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = ['anime_id', 'title', 'rating', 'image_url', 'description']


class SavedAnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedAnime
        fields = ['user', 'anime', 'type']
