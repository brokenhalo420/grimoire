from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from .models import Anime, SavedAnime
from .serializers import AnimeSerializer, SavedAnimeSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

@api_view(['GET',])
def get_anime_list(request):
    anime = Anime.objects.all()
    animeSerializer = AnimeSerializer(anime, many=True)
    return JsonResponse(animeSerializer.data, safe=False)

@api_view(['GET',])
def get_top_hundred_anime(request, number):
    anime = sorted(Anime.objects.all(), key = lambda anime: anime.rating, reverse = True)[:number]
    animeSerializer = AnimeSerializer(anime, many=True)
    return JsonResponse(animeSerializer.data, safe=False)

@api_view(['GET',])
def get_anime_details(request, title):
    try:
        anime = Anime.objects.get(title = title)
    except Anime.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    serializer = AnimeSerializer(anime)
    return Response(serializer.data, status = status.HTTP_200_OK)


def add_anime_to_favorites(request, anime_id, username):
    print(f'username: {username}')
    try:
        user = User.objects.get(username = username)
    except User.DoesNotExist:
        return JsonResponse(data={}, status= status.HTTP_402_PAYMENT_REQUIRED)
    
    try:
        anime = Anime.objects.get(anime_id=anime_id)
    except Anime.DoesNotExist:
        return JsonResponse(data={}, status= status.HTTP_403_FORBIDDEN)
    
    anime_in_db, created = SavedAnime.objects.get_or_create(
                anime_id=anime.id,
                type='Favorite',
                user_id=user.id,
                defaults={
                    'anime_id': anime.id,
                    'user_id': user.id,
                    'type': 'Favorite'
                }
            )

    if not created:
        anime_in_db.anime_id = anime.id
        anime_in_db.user_id = user.id
        anime_in_db.type = 'Favorite'
        anime_in_db.save()

    return JsonResponse(data={}, status = status.HTTP_200_OK)

def add_anime_to_watch_later(request, anime_id, username):
    print(f'username: {username}')
    try:
        user = User.objects.get(username = username)
    except User.DoesNotExist:
        return JsonResponse(data={}, status= status.HTTP_402_PAYMENT_REQUIRED)
    
    try:
        anime = Anime.objects.get(anime_id=anime_id)
    except Anime.DoesNotExist:
        return JsonResponse(data={}, status= status.HTTP_403_FORBIDDEN)
    
    anime_in_db, created = SavedAnime.objects.get_or_create(
                anime_id=anime.id,
                type='Watch Later',
                user_id=user.id,
                defaults={
                    'anime_id': anime.id,
                    'user_id': user.id,
                    'type': 'Watch Later'
                }
            )

    if not created:
        anime_in_db.anime_id = anime.id
        anime_in_db.user_id = user.id
        anime_in_db.type = 'Watch Later'
        anime_in_db.save()

    return JsonResponse(data={}, status = status.HTTP_200_OK)


def add_anime_to_watched(request, anime_id, username):
    print(f'username: {username}')
    try:
        user = User.objects.get(username = username)
    except User.DoesNotExist:
        return JsonResponse(data={}, status= status.HTTP_402_PAYMENT_REQUIRED)
    
    try:
        anime = Anime.objects.get(anime_id=anime_id)
    except Anime.DoesNotExist:
        return JsonResponse(data={}, status= status.HTTP_403_FORBIDDEN)
    
    anime_in_db, created = SavedAnime.objects.get_or_create(
                anime_id=anime.id,
                type='Watched',
                user_id=user.id,
                defaults={
                    'anime_id': anime.id,
                    'user_id': user.id,
                    'type': 'Watched'
                }
            )

    if not created:
        anime_in_db.anime_id = anime.id
        anime_in_db.user_id = user.id
        anime_in_db.type = 'Watched'
        anime_in_db.save()

    return JsonResponse(data={}, status = status.HTTP_200_OK)
    
@api_view(['GET',])
def get_favorites(request, username):
    user = User.objects.get(username=username)
    print(user)
    savedAnime = list(map(lambda x: x.anime_id, SavedAnime.objects.all().filter(user_id=user.id).filter(type='Favorite')))
    savedAnime = list(map(lambda x: Anime.objects.get(id=x), savedAnime))
    animeSerializer = AnimeSerializer(savedAnime, many=True)
    return JsonResponse(animeSerializer.data, safe=False)

@api_view(['GET',])
def get_watch_later(request, username):
    user = User.objects.get(username=username)
    print(user)
    savedAnime = list(map(lambda x: x.anime_id, SavedAnime.objects.all().filter(user_id=user.id).filter(type='Watch Later')))
    savedAnime = list(map(lambda x: Anime.objects.get(id=x), savedAnime))
    animeSerializer = AnimeSerializer(savedAnime, many=True)
    return JsonResponse(animeSerializer.data, safe=False)

@api_view(['GET',])
def get_watched(request, username):
    user = User.objects.get(username=username)
    print(user)
    savedAnime = list(map(lambda x: x.anime_id, SavedAnime.objects.all().filter(user_id=user.id).filter(type='Watched')))
    savedAnime = list(map(lambda x: Anime.objects.get(id=x), savedAnime))
    animeSerializer = AnimeSerializer(savedAnime, many=True)
    return JsonResponse(animeSerializer.data, safe=False)


def remove_anime_from_favorites(request, anime_id, username):
    try:
        user = User.objects.get(username = username)
    except User.DoesNotExist:
        return JsonResponse(data={}, status= status.HTTP_404_NOT_FOUND)
    
    try:
        anime = Anime.objects.get(anime_id=anime_id)
    except Anime.DoesNotExist:
        return JsonResponse(data={}, status= status.HTTP_404_NOT_FOUND)
    
    anime_in_db, created = SavedAnime.objects.all().filter(user_id=user.id).filter(anime_id=anime.id).filter(type='Favorite').delete()
    return JsonResponse(data={}, status = status.HTTP_200_OK)


def remove_anime_from_watch_later(request, anime_id, username):
    try:
        user = User.objects.get(username = username)
    except User.DoesNotExist:
        return JsonResponse(data={}, status= status.HTTP_404_NOT_FOUND)
    
    try:
        anime = Anime.objects.get(anime_id=anime_id)
    except Anime.DoesNotExist:
        return JsonResponse(data={}, status= status.HTTP_404_NOT_FOUND)
    
    anime_in_db, created = SavedAnime.objects.all().filter(user_id=user.id).filter(anime_id=anime.id).filter(type='Watch Later').delete()
    return JsonResponse(data={}, status = status.HTTP_200_OK)

def remove_anime_from_watched(request, anime_id, username):
    try:
        user = User.objects.get(username = username)
    except User.DoesNotExist:
        return JsonResponse(data={}, status= status.HTTP_404_NOT_FOUND)
    
    try:
        anime = Anime.objects.get(anime_id=anime_id)
    except Anime.DoesNotExist:
        return JsonResponse(data={}, status= status.HTTP_404_NOT_FOUND)
    
    anime_in_db, created = SavedAnime.objects.all().filter(user_id=user.id).filter(anime_id=anime.id).filter(type='Watched').delete()
    return JsonResponse(data={}, status = status.HTTP_200_OK)