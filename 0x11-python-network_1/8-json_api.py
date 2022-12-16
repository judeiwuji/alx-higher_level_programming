#!/usr/bin/python3
"""
takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.

Requirements:
 - The letter must be sent in the variable q
 - If no argument is given, set q=""
 - If the response body is properly JSON formatted and not empty, display
   the id and name like
    - this: [<id>] <name>
        Otherwise:
        - Display Not a valid JSON if the JSON is invalid
        - Display No result if the JSON is empty
 - You must use the package requests and sys
 - You are not allowed to import packages other than requests and sys
"""
import requests
from sys import argv


def main():
    """Read Header"""
    url = "http://0.0.0.0:5000/search_user"
    query = ""
    if len(argv) > 1:
        query = argv[1]
    url = url + "?q={}".format(query)
    res = requests.post(url)

    try:
        if res.text:
            data = res.json()
            print("[{}] {}".format(data['id'], data['name']))
        else:
            print("No result")
    except requests.exceptions.JSONDecodeError as error:
        print("Not a valid JSON")


if __name__ == "__main__":
    main()
