#!/usr/bin/python3
"""A function that queries the Reddit API and
prints the titles of the first 10 hot posts
listed for a given subreddit."""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    params = {"limit": 10}
    
    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        response.raise_for_status()  # Raise an exception for HTTP errors (e.g., 404)
        data = response.json()
        for post in data["data"]["children"]:
            print(post["data"]["title"])
    except requests.exceptions.HTTPError as err:
        print("None")  # Invalid subreddit or other HTTP error
