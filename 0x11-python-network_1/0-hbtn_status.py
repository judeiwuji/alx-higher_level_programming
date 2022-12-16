#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""
from urllib.request import Request
from urllib.request import urlopen


def main():
    """Main: function"""
    req = Request("https://alx-intranet.hbtn.io/status")
    with urlopen(req) as res:
        content = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode("utf-8")))


if __name__ == "__main__":
    main()
