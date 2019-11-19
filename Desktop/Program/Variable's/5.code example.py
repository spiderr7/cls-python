a=10
def outer():
    global a
    a=32
    print("Control entered into outer function")
    def inner():
        global a
        print(a)
        a=15
        print("Control entered into inner function")
        print("Control leaving inner function")
    print(a)
    inner()
    print("Control leaving outer funtion")
print(a)
outer()
print(a)
    
