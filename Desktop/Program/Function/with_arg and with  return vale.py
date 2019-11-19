a,b=10,20
print(a,b)
def swap(a,b):
    a,b=b,a
    return a,b
print(a,b)
a,b=swap(a,b)
print(a,b)
