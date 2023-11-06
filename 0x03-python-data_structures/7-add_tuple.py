#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    val1 = tuple_a[0] if len(tuple_a) > 0 else 0
    val2 = tuple_a[1] if len(tuple_a) > 1 else 0
    val3 = tuple_b[0] if len(tuple_a) > 0 else 0
    val4 = tuple_b[1] if len(tuple_a) > 1 else 0
    return(val1, val3, val2, val4)
