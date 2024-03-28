#!/usr/bin/python3
""" module doc """
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    payload = {'email': email}
    r = requests.get(url, params=payload)
    print(r.text)
