#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    value = 0
    result = []
    while value < list_length:
        res = 0
        try:
            res = my_list_1[value] / my_list_2[value]
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            result.append(res)
            value += 1
    return result
