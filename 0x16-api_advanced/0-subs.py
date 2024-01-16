#!/usr/bin/python3
"""function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit"""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit."""
    header = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:121.0)"
    }
    resp = requests.get(f"https://www.reddit.com/r/{subreddit}/about.json",
                        headers=header, allow_redirects=False)
    if resp.status_code == 404:
        return 0
    try:
        return resp.json().get("data").get("subscribers")
    except requests.exceptions.JSONDecodeError:
        return 0
