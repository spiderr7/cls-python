#before decorater

import time
def square():
    start=time.time()
    for i in range(100000):
        res=i**2
    end=time.time()
    print("Total time taken is",end-start)

def cube():
    start=time.time()
    for i in range(100000):
        res=i**3
    end=time.time()
    print("Total time taken is",end-start)

def pow4():
    start=time.time()
    for i in range(100000):
        res=i**4
    end=time.time()
    print("Toatl time taken is",end-start)

square()
cube()
pow4()
