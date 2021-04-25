#!/bin/env/python3
import time
import calendar


def time_operation():
    print("#" * 50)
    ticks = time.time()
    print ("Number of ticks since 12:00am, January 1, 1970:", ticks)
    print("#" * 50)
    print("Local Time:", time.localtime())
    print("#" * 50)
    print("Local Time:", time.localtime(time.time()))
    print("#" * 50)
    localtime = time.asctime( time.localtime(time.time()) )
    print ("Local current time :", localtime)        
    print("#" * 50)
  
    
def calendar_operation():
    print("#" * 50)
    cal = calendar.month(2021, 2)
    print ("Here is the calendar:")
    print (cal)
    print("#" * 50)    
    

def date_time():
    time_operation()    
    calendar_operation()
    