#!/usr/bin/python3
"""function that queries the Reddit API and prints the titles of the first 10
hot posts listed for a given subreddit"""
import requests


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts listed."""
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    response = requests.get(url, headers=headers, params={"limit": 10},
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    data = response.json().get("data")
    [print(c.get("data").get("title")) for c in data.get("children")]
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
            'User-Agent': 'Mozilla/5.0'
    }
    params = {
            'limit': 10
    }
    response = requests.get(url,
                            headers=headers,
                            params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return
    res = response.json()
    hot_posts = res['data']['children']
    if len(hot_posts) == 0:
        print(None)
    else:
        for post in hot_posts:
            print(post['data']['title'])
