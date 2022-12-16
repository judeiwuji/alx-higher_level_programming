#!/usr/bin/python3
"""
fetches https://alx-intranet.hbtn.io/status
"""
import requests


def main():
    """Fetch data"""
    res = requests.get("https://alx-intranet.hbtn.io/status")
    content = res.text
    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))


if __name__ == "__main__":
    main()
