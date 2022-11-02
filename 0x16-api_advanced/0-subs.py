#!/usr/bin/python3
"""returns the number of subscribers (not active users, total subscribers) for a given subreddit"""
import requests


def number_of_subscribers(subreddit):
    headers = {'User-Agent': 'Linux/client/0.0'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, headers=headers)
    if response.status_code == 404:
        return 0
    else:
        subsciber = response.json()['data']['subscribers']
        return subsciber
