#!/bin/env/python3

from decorator import printer
from division import division
from func_ret import called_func
from func_alias import third
from lambda_ex import lambda_func
from list_map_dict_ex import list_map_dict
from string_ex import str_operation
from date_time import date_time


def main():    
  printer("Hello Decorator", 10)
  division(5, 2)
  called_func(0)  
  third("I am the alias of first()")
  lambda_func()  
  str_operation()
  list_map_dict()
  date_time()
  
if __name__ == "__main__":
    main()
    
