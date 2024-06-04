#!/usr/bin/python3
"""Module for task 1: Get top 10 hot posts of a subreddit"""


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the top 10 hot posts
    for the given subreddit.
    """
    import requests

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "My-User-Agent"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code >= 300:
        print('None')
    else:
        for post in response.json().get("data", {}).get("children", []):
            print(post.get("data", {}).get("title", "None"))
