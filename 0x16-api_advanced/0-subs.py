#!/usr/bin/python3
"""returns the number of subscribers (not active users, total subscribers) for a given subreddit"""
import requests


def number_of_subscribers(subreddit):
    """Gets number of subscribers
       Returns:
           number of subscribers if valid, 0 otherwise
    """
    base_url = 'https://api.reddit.com/r/'
    headers = {'User-Agent': 'my-app/0.0.1'}
    response = requests.get(
        '{}{}/about'.format(
            base_url, subreddit), headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0

    about_dict = response.json()

    return about_dict['data']['subscribers']
