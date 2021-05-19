#!/usr/bin/python3
"""a function that queries the Reddit API and prints the titles of the first
10 hot posts listed for a given subreddit"""
import json
import requests


def top_ten(subreddit):
    """ prints top ten titles """
    url = "http://api.reddit.com/r/{}/hot?limit=10".format(subreddit)
    headers = {
        'User-Agent': 'nugget'
    }
    x = requests.get(url, headers=headers)
    if not x:
        print(None)
    else:
        data = x.json()
        i = data.get('data').get('children')
        for r in i:
            s = r.get('data').get('title')
            print(s)
