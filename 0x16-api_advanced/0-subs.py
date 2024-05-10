#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "MyAPI/0.1"}
    response = requests.get(url, headers=headers)
    
    # Check for errors
    if response.status_code != 200:
        return 0
    
    # Parse JSON response
    data = response.json()
    subscribers = data["data"]["subscribers"]
    
    return subscribers

if __name__ == "__main__":
    subreddit = input("Enter subreddit: ")
    print(number_of_subscribers(subreddit))
