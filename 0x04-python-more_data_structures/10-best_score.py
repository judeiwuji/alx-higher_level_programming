#!/usr/bin/python3


def best_score(a_dictionary):
    best = {'name': None, 'score': 0}

    if a_dictionary is not None:
        for k, v in a_dictionary.items():
            if v > best['score']:
                best['name'] = k
                best['score'] = v
    return best['name']
