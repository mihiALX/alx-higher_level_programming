#!/usr/bin/python3
def safe_print_division(x, y):
    try:
        z = x / y
        print("Inside result: {:.1f}".format(z))
    except:
        z = None
        print("Inside result: {}".format(z))
    finally:
        return z
