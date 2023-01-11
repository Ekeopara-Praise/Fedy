# Lets  start
import requests
import pandas as pd
from fastapi import FastAPI


# define the API key
api_key = '790713ded66fe0dd637dd61f70925146'
# headers contain the api key.
headers = {'Authorization': 'Bearer {}'.format(api_key)}


# search_api_url = f'https://api.springernature.com/metadata/json?api_key=790713ded66fe0dd637dd61f70925146&q=Technology&s=1&p={p}'

search_api_url = 'https://api.springernature.com/metadata/json'

payload = {'api_key': api_key, 'q': 'Technology', 'p': 2}

response = requests.get(search_api_url, headers=headers, params=payload) # timeout=2)

res = response.json()

# print(response.url)
# # print(response.headers)
# print(response.json())
# print(response.status_code)

print(res['records'])
