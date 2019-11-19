#WITH GLOBAL VARIABLE
a,b=10,20
print(a,b)
def swap():
    global a,b
    a,b=b,a
swap()
print(a,b)
