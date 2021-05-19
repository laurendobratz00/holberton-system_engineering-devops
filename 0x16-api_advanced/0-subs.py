#!/usr/bin/python3
""" a function that queries the Reddit API and returns the # of subscribers """
import requests


def number_of_subscribers(subreddit):
    """ returns number of subscribers """
    url = "http://api.reddit.com/r/{}/about".format(subreddit)
    headers = {
        'User-Agent': 'nugget'
    }
    x = requests.get(url, headers=headers)
    if not x:
        return 0
    else:
        data = x.json()
        count = data.get('data').get('subscribers')
        return count
