#!/usr/bin/python3
"""
takes your GitHub credentials (username and password) and uses
the GitHub API to display your id

Requirements:
 - You must use Basic Authentication with a personal access token
   as password to access to your information (only read:user
   permission is needed)
 - The first argument will be your username
 - The second argument will be your password (in your case,
   a personal access token as password)
 - You must use the package requests and sys
 - You are not allowed to import packages other than requests and sys
 - You don’t need to check arguments passed to the script (number or type)
"""
import requests
from sys import argv


def main():
    """Github Auth"""
    url = "https://api.github.com/user"
    username = argv[1]
    password = argv[2]
    res = requests.get(url, auth=(username, password))
    if res.status_code == 200:
        try:
            data = res.json()
            id = None
            if len(data) > 0:
                id = "{}".format(data['id'])
            print(id)
        except ValueError:
            pass
    else:
        print(None)


if __name__ == "__main__":
    main()
