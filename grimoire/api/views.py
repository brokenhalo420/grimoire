from django.shortcuts import render
from django.http import JsonResponse
from .models import User, Anime, SavedAnime
from .serializers import UserSerializer, AnimeSerializer, SavedAnimeSerializer
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET'])
def users_list(request):
    users = User.objects.all()
    userSerializer = UserSerializer(users, many=True)
    return JsonResponse(userSerializer.data, safe=False)


def anime_list(request):
    anime = Anime.objects.all()
    animeSerializer = AnimeSerializer(anime, many=True)
    return JsonResponse(animeSerializer.data, safe=False)

def top_hundred_anime(request):
    anime = sorted(Anime.objects.all(), key = lambda anime: anime.rating, reverse = True)
    animeSerializer = AnimeSerializer(anime, many=True)
    return JsonResponse(animeSerializer.data, safe=False)