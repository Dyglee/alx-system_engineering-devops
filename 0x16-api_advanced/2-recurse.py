#!/usr/bin/python3
"""Module for task 2: Recursively get all hot posts of a subreddit"""


def recurse(subreddit, hot_list=[], count=0, after=None):
    """
    Queries the Reddit API and returns a list of titles of all hot posts
    for the given subreddit using recursion.
    """
    import requests

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "My-User-Agent"}
    params = {"count": count, "after": after}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    if response.status_code >= 400:
        return None

    hot_list.extend([post.get("data", {}).get("title", "None")
                     for post in response.json().get("data", {}).get("children", [])])
    after = response.json().get("data", {}).get("after")
    if not after:
        return hot_list

    return recurse(subreddit, hot_list, count=len(hot_list), after=after)
