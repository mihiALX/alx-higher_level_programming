#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):

    value = printed_ints = 0
    while True:
        try:
            if value < x:
                print("{:d}".format(my_list[value]), end='')
                value += 1
                printed_ints += 1
            else:
                print()
                return printed_ints
        except (ValueError, TypeError):
            value += 1
