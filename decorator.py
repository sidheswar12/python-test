#!/bin/env/python3

def start(func):
  def inner(*args, **kwargs):
    print("#" * 50)
    func(*args, **kwargs)
    print("#" * 50)
  return inner

def percent(func):
  def inner(*args, **kwargs):
    print("*" * 50)
    func(*args, **kwargs)
    print("*" * 50)
  return inner

def calculate(func):
  def inner(*args, **kwargs):      
    func(*args, **kwargs)
    print("I am power of x:", args[1]*args[1])
  return inner
  
@start
@percent
@calculate
def printer(msg, x):
  print(msg)  
