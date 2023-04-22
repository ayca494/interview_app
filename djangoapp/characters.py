import requests
from django.http import JsonResponse
import hashlib
import time
def character_list(request):
    public_key = 'df4c7924382be16818ea827cac0cd790'
    private_key = '4879dd23a4eb64da5b416b66c7607dc6087b0ac9'
    url = 'https://gateway.marvel.com/v1/public/characters'

    
    timestamp = str(time.time()) # current Unix time in seconds
    hash = hashlib.md5(f"{timestamp}{private_key}{public_key}".encode('utf-8')).hexdigest()

    # Make the API request with the appropriate query parameters
    response = requests.get(url, params={
        'apikey': public_key,
        'ts': '1',
        'hash': hash,
        'limit': 20
    })

    # Parse the API response and extract the characters data
    characters = response.json()['data']['results']

    # Return the characters as JSON
    return JsonResponse({'characters': characters})
