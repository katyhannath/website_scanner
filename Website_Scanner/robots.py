#!/usr/bin/env python3
import urllib.request
import io

def get_robots(url):
    if url.endswith('/'):
        path = url
    else:
        path = url + '/'

    req = urllib.request.Request(path + 'robots', data=None)
    # data = io.TextIOWrapper(req, encoding = 'utf-8')
    with urllib.request.urlopen(req) as response:
        return response.read()

#print(get_robots('https://www.coventry.ac.uk/'))
