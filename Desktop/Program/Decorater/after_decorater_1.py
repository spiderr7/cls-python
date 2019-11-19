#After decorater

import time
def timer(func):
    def inner():
        start=time.time()
        func()
        end=time.time()
        print("Toatl time taken is",end-start)
    return inner

@timer
def square():
    for i in range(100000):
        res=i**2

@timer
def cube():
    for i in range(100000):
        res=i**3

@timer
def pow4():
    for i in range(100000):
        res=i**4

square()
cube()
pow4()
