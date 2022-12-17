#!/usr/bin/python3
"""
Requirements:
 - The first argument will be the repository name
 - The second argument will be the owner name
 - You must use the packages requests and sys
 - You are not allowed to import packages other than requests and sys
 - You don’t need to check arguments passed to the script (number or type)
"""
import requests
from sys import argv


def main():
    """Github commits"""
    repo = argv[1]
    owner = argv[2]
    url = "https://api.github.com/repos/{}/{}/commits?per_page=10".\
          format(owner, repo)

    res = requests.get(url)
    if res.status_code == 200:
        try:
            json = res.json()
            for data in json:
                author = "{}".format(data['commit']['author']['name'])
                sha = "{}".format(data['sha'])
                print("{}: {}".format(sha, author))
        except ValueError:
            pass
    else:
        print(None)


if __name__ == "__main__":
    main()
