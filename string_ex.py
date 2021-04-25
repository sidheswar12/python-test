#!/bin/env/python3

def string_split(s):
    print("#" * 50)  
    print("{} : {}".format(s, s.split()))
    print("#" * 50)
          
def remove_whitespace(s):
    print("#" * 50)
    print("'{}': '{}'".format(s, s.strip()))
    print("#" * 50)

def fstream_func(name, company):
    print("#" * 50)
    print(f'I am {name}, working at {company} company')
    print("#" * 50)
    
def string_format():
    print("#" * 50)
    print("*****String arrange using format indexing*****") 
    print("Hello {0} {3} {1} {2}".format("Me", "my", "Son", "and"))
    print("#" * 50)
    
def str_slicing(s):
    print("#" * 50)
    print("Original String: ", s)
    print(s[1:])
    print(s[1:3])
    print(s[:2])
    print(s[:-1])
    print(s[-2])
    print(s[::-1])
    print('i' + s[1:])
    print("#" * 50)
    
          
def str_operation():
    string_split("String is not mutable cannot change using index so, I am going to split as list")
    remove_whitespace(" remove first and last white space ")
    fstream_func("Sidheswar", "ABC")
    string_format()
    str_slicing("Hello")  
    