import requests
from requests.auth import HTTPBasicAuth
from credentials import API_URL, CLIENT_ID, HEADER_NAME

parameters = {'ranking_type': 'all', 'fields': 'id,title,main_picture,mean,genres', 'offset': 0}
headers = {f'{HEADER_NAME}': f'{CLIENT_ID}'}

r = requests.get(f'{API_URL}anime/ranking', params = parameters, headers=headers)

print(r.content)
