import requests
from requests.auth import HTTPBasicAuth
from credentials import API_URL, CLIENT_ID, HEADER_NAME
from models import Anime

def get_top_anime(offset=0):
    parameters = {'ranking_type': 'all', 'fields': 'id,title,main_picture,mean', 'offset': offset}
    headers = {f'{HEADER_NAME}': f'{CLIENT_ID}'}

    r = requests.get(f'{API_URL}anime/ranking', params = parameters, headers=headers)
    return r.content

def get_anime_by_title(title):
    parameters = {'q': f'{title}', 'fields': 'id,title,main_picture,mean', 'offset': 0}
    headers = {f'{HEADER_NAME}': f'{CLIENT_ID}'}

    r = requests.get(f'{API_URL}anime', params = parameters, headers=headers)
    return r.json()['data']
