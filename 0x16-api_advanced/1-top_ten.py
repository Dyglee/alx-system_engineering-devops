#!/usr/bin/python3
"""
1-top_ten
"""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("None")
        return

    data = response.json()
    if 'data' in data and 'children' in data['data']:
        posts = data['data']['children']
        for post in posts:
            print(post['data']['title'])
    else:
        print("None")
