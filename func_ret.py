#!/bin/env/python3

def called_func(x):
    def inner():
      print("Return inner function:", x)   
    
    def hello_print():
        print("Hello: ", x)
      
    if x == 0:
      return inner
    else:
      return hello_print
      