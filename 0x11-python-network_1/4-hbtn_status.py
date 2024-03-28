#!/usr/bin/python3
""" module doc """
import requests


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    r = requests.get(url)
    data = r.text
    resType = type(data)
    print(f"Body response:\n\t- type: {resType}\n\t\
- content: {data}")
