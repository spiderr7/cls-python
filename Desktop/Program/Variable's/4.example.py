def outer():
    print("Control entered into outer funtion")
    def inner():
        print("Control entered into inner funtion")
        print("Control leaving ineer function")
    print(inner)
    inner()
    print("Control leaving outer function")
outer()
