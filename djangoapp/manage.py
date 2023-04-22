#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import hashlib
import time
import requests
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render

def main():
    
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoapp.settings')
    try:
        from django.core.management import execute_from_command_line

        PUBLIC_KEY = 'df4c7924382be16818ea827cac0cd790'
        PRIVATE_KEY = '4879dd23a4eb64da5b416b66c7607dc6087b0ac9'

        timestamp = str(time.time()) # current Unix time in seconds
        hash = hashlib.md5(f"{timestamp}{PRIVATE_KEY}{PUBLIC_KEY}".encode('utf-8')).hexdigest()

        url = 'https://gateway.marvel.com/v1/public/characters'
        page = 1
        response = requests.get(url, params={
            'apikey': PUBLIC_KEY,
            'ts': timestamp,
            'hash': hash,
            'offset': (page - 1) * 20, 
            'limit': 20
        })
        characters = response.json()['data']['results']
        paginator = Paginator(characters, 20)
        character_page = paginator.page(page)
    # render(request, 'character_list.html', {'characters': character_page})

      
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

