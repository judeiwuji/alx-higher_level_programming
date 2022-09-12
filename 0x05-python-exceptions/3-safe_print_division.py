#!/usr/bin/python3

def safe_print_division(a, b):
    qoutient = None
    try:
        qoutient = a / b
    except ZeroDivisionError:
        pass
    finally:
        print("Inside result: {}".format(qoutient))
    return qoutient
