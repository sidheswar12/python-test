#!/bin/env/python3

def smart_division(func):
    def inner(a, b):        
        if b == 0:
            print("Whoops! cannot divide")
            return
        return func(a, b)
    return inner


@smart_division
def division(a, b):
    print("Division: {} / {} = {}".format(a, b, a/b))
