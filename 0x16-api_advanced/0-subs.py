#!/usr/bin/python3
""" function that queries the Reddit API """
import requests


def number_of_subscribers(subreddit):
    subreds = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    red_req = requests.get(subreds, headers={'User-Agent': 'lee'})
    if (red_req.status_code == requests.codes.ok):
        json_full = red_req.json()
        return (json_full['data']['subscribers'])
    else:
        return (0)
