#!/usr/bin/python3


def multiple_returns(sentence):
    c = None
    if sentence is None:
        return
    if len(sentence) > 0:
        c = sentence[0]
    return (len(sentence), c)
