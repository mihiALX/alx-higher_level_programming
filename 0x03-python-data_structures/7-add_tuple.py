#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    value1 = tuple_a[0] if len(tuple_a) > 0 else 0
    value2 = tuple_a[1] if len(tuple_a) > 1 else 0
    value3 = tuple_b[0] if len(tuple_a) > 0 else 0
    value4 = tuple_b[1] if len(tuple_a) > 1 else 0
    return(value1, value3, value2, value4)
