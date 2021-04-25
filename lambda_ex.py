
#!/bin/env/python3

def lambda_func():
    print("Power of each elements [1,2,3] using lambda:", list(map(lambda x:x*x, [1,2,3])))
    power = lambda x, y: x ** y
    print("{} raise {} using lambda:".format(2, 3), power(2, 3))
    