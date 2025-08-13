import requests
from pprint import pprint
import json
url = 'https://randomuser.me/api'
params01 = {
    'results':20,
    'gender':'male'
}

params02 = {
    'results':20,
    'gender':'female'
}

respose = requests.get(url, parms01=params02)

with open("data/db.json", "w") as f:
    
