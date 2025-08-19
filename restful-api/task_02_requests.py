#!/usr/bin/python3
"""
Test requests library
"""
import requests
import csv

url = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """
    fetch and print posts
    """
    r = requests.get(url)
    print(f"Status Code: {r.status_code}")
    for post in r.json():
        print(post["title"])


def fetch_and_save_posts():
    """
    Fetch and save posts
    """
    r = requests.get(url)
    posts = r.json()
    keys = ["id", "title", "body"]
    with open("posts.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        for post in posts:
            writer.writerow(
                    {"id": post["id"],
                     "title": post["title"],
                     "body": post["body"]}
                    )
