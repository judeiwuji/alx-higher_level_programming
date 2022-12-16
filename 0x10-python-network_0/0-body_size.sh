#!/usr/bin/env bash
# takes in a URL, sends a request to that URL, and displays
# the size of the body of the response
curl -silent "$1" | wc --bytes
