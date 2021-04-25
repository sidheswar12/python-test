#!/bin/env/python3

def power(x):
  return x*x

def multiple_type_elements_list():
    lst = [1, 'Hello', 1.2]
    print("#" * 50)
    print(lst)
    print("#" * 50)

def map_func():
    y = list(map(power, [1,2,3]))
    print("#" * 50)
    print("Calculate power of each elements [1,2,3] without loop:", y) 
    print("#" * 50)
    
def list_operation():
  print("#" * 50)
  lst = ['Jan', 'Feb', 'Mar']
  print("Before Append:", lst)
  lst.append('Apr')
  print("After Append:", lst)
  lst.reverse()
  print("After Reverse:", lst)
  lst.sort()
  print("After Sort:", lst)
  lst.pop()
  print("After Pop:", lst)
    
  print("Range of list:", range(len(lst)))
  print("#" * 50)
        
def loop_operation():
  lst = ['Jan', 'Feb', 'Mar']
  print("#" * 50)
  for count, val in enumerate(lst):
    print(count, ":", val)
  print("#" * 50)

  lst = [1, 2, 3, 4, 5]
  for i in range(len(lst)):
    print(i, ":", lst[i])
  print("#" * 50)
    
    
def dict_operation():
  dict = {
    "brand": "SSS",
    "service": "ABC",
    "location": "GER",
    }
  print("#" * 50)
  print(dict["brand"])
  print("#" * 50)
  for key in dict:    
    print(dict[key])
  print("%" * 50)
  
  dict = {
    '1': {'name': 'Tanu', 'age':'35', 'location': 'Ger'},
    '2': {'name': 'Manu', 'age':'6', 'location': 'Ger'},
    '3': {'name': 'Chanu', 'age': '30', 'location':'Ger'},
    }
  print("#" * 50)
  for dt in dict:
    for key in dict[dt]:      
      print(dict[dt][key])
    print("#" * 50) 
  print("#" * 50)
  

def tuple_operation():
  tup1 = ('Computer', 'Science', 2003, 75.5)
  tup2 = (1, 2, 3, 4, 5 )
  tup3 = "a", "b", "c"
  print("#" * 50)
  print("tup1[0]: ", tup1[0])
  print("tup2[1:5]: ", tup2[1:5])
  print("tup3[1:5]: ", tup3[1:2])
  print("#" * 50)
  tup = tup1 + tup2
  print(tup)
  print("#" * 50)
  
  print("#" * 50)
  print("Length of tup:", len(tup))
  print("#" * 50)
  print("Length of Touple:", len((1,3,4)))
  print("#" * 50)
  print("Add tuple:", (1,2,3) + (4,5,6))
  print("#" * 50)
  print("Repetition:", ('Hi!',)*4)
  print("#" * 50)
  print("Check 3 is available or not:", 3 in (1,9,4, 6))
  print("#" * 50)
  print("Check India is available or not:", 'India' in ('Germany', 'Poland', 'France', 'India', 'USA'))
  print("#" * 50)
  for x in (1,4,6):
    print(x, end=' ')
  print("#" * 44)
  print("#" * 50)
  T = ('C++', 'Python', 'Java')
  print(T[2])
  print(T[-2])
  print(T[1:])
  print("#" * 50)
  
  print("Len:", len(T))
  print("Max element of the tuple:", max(T))
  print("Max element of the tuple:",max(tup2))
  print("#" * 50)
  print("Min element of the tuple:", min(T))
  print("Min element of the tuple:",min(tup2))
  print("#" * 50)
  
  lst = [2,4,6,8,9,1]
  tpl = tuple(lst)
  print("Converted to Tuple:", tpl)
  print("#" * 50)
  
  del tup
  print ("After deleting tup no more tup available")
  print("#" * 50)
    
  
    
def list_map_dict():
  multiple_type_elements_list()
  map_func()
  list_operation()
  loop_operation()
  dict_operation()
  tuple_operation()
        