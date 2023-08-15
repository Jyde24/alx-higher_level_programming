#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if my_list:
        list_reversed = reversed(my_list)
        for i in list_reversed:
            print(f"{i:d}")
