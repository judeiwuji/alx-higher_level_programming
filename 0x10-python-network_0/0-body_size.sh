#!/bin/bash
# takes in a URL, sends a request to that URL, and displays
curl -s "$1" | wc --bytes
