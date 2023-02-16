from django.shortcuts import render
from django.http import JsonResponse
from .models import User, Anime, SavedAnime
from .serializers import UserSerializer, AnimeSerializer, SavedAnimeSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

@api_view(['GET',])
def get_users_list(request):
    users = User.objects.all()
    userSerializer = UserSerializer(users, many=True)
    return JsonResponse(userSerializer.data, safe=False)

@api_view(['GET',])
def get_anime_list(request):
    anime = Anime.objects.all()
    animeSerializer = AnimeSerializer(anime, many=True)
    return JsonResponse(animeSerializer.data, safe=False)

@api_view(['GET',])
def get_top_hundred_anime(request):
    anime = sorted(Anime.objects.all(), key = lambda anime: anime.rating, reverse = True)
    animeSerializer = AnimeSerializer(anime, many=True)
    return JsonResponse(animeSerializer.data, safe=False)

@api_view(['POST',])
def create_user(request):
    serializer = UserSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    
    return Response(status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET',])
def get_anime_details(request, title):
    try:
        anime = Anime.objects.get(title = title)
    except Anime.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    serializer = AnimeSerializer(anime)
    return Response(serializer.data, status = status.HTTP_200_OK)