a,b=1,2
print(a,b)
def outer():
    a,b=10,20
    print(a,b)
    def swap():
        nonlocal a,b
        a,b=b,a
        print(a,b)
    print(a,b)
    swap()
    print(a,b)
outer()
print(a,b)
