import requests
from requests.auth import HTTPBasicAuth
from . import credentials 
from .import models

def get_top_anime(offset=0, limit=100):
    parameters = {'ranking_type': 'all', 'fields': 'id,title,main_picture,mean,synopsis', 'offset': offset, 'limit': limit}
    headers = {f'{credentials.HEADER_NAME}': f'{credentials.CLIENT_ID}'}

    r = requests.get(f'{credentials.API_URL}anime/ranking', params = parameters, headers=headers)
    return r.json()

def get_anime_by_title(title):
    parameters = {'q': f'{title}', 'fields': 'id,title,main_picture,mean,synoposis', 'offset': 0}
    headers = {f'{credentials.HEADER_NAME}': f'{credentials.CLIENT_ID}'}
    r = requests.get(f'{credentials.API_URL}anime', params = parameters, headers=headers)
    return r.json()['data']
