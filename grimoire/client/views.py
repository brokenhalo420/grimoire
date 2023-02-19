from django.shortcuts import render
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import requests
from utility.serializers import AnimeSerializer
from utility.deserializers import parse_anime_list

# Create your views here.

@login_required(login_url='/auth/login/')
@api_view(['GET',])
def home(request):
    return render(request, 'client/search.html', {})

@login_required(login_url='/auth/login')
@api_view(['GET',])
def get_ranking(request, number):
    serializer = AnimeSerializer()
    anime = requests.get(f'http://127.0.0.1:8000/api/ranked/{number}').json()
    return render(request, 'client/ranking.html', {
        'anime_list': parse_anime_list(anime)
    })

@csrf_protect
@login_required(login_url='/auth/login')
def add_to_favorite(request, anime_id):
    requests.get(f'http://127.0.0.1:8000/api/favorite/{anime_id}/{request.user.username}')
    return get_ranking(request, 100)


@csrf_protect
@login_required(login_url='/auth/login')
def add_to_watch_later(request, anime_id):
    requests.get(f'http://127.0.0.1:8000/api/watch_later/{anime_id}/{request.user.username}')
    return get_ranking(request, 100)


@csrf_protect
@login_required(login_url='/auth/login')
def add_to_watched(request, anime_id):
    requests.get(f'http://127.0.0.1:8000/api/watched/{anime_id}/{request.user.username}')
    return get_ranking(request, 100)

@login_required(login_url='auth/login')
def get_favorites(request):
    serializer = AnimeSerializer()
    anime = requests.get(f'http://127.0.0.1:8000/api/favorites/{request.user.username}').json()
    return render(request, 'client/favorites.html', {
        'anime_list': parse_anime_list(anime)
    })

@login_required(login_url='auth/login')
def get_watch_later(request):
    serializer = AnimeSerializer()
    anime = requests.get(f'http://127.0.0.1:8000/api/watch_later/{request.user.username}').json()
    return render(request, 'client/watch_later.html', {
        'anime_list': parse_anime_list(anime)
    })

@login_required(login_url='auth/login')
def get_watched(request):
    serializer = AnimeSerializer()
    anime = requests.get(f'http://127.0.0.1:8000/api/watched/{request.user.username}').json()
    return render(request, 'client/watched.html', {
        'anime_list': parse_anime_list(anime)
    })

@login_required(login_url='auth/login')
def remove_from_favorites(request, anime_id):
    requests.get(f'http://127.0.0.1:8000/api/favorites/remove/{anime_id}/{request.user.username}')
    return get_favorites(request)

@login_required(login_url='auth/login')
def remove_from_watch_later(request, anime_id):
    requests.get(f'http://127.0.0.1:8000/api/watch_later/remove/{anime_id}/{request.user.username}')
    return get_favorites(request)

@login_required(login_url='auth/login')
def remove_from_watched(request, anime_id):
    requests.get(f'http://127.0.0.1:8000/api/watched/remove/{anime_id}/{request.user.username}')
    return get_favorites(request)