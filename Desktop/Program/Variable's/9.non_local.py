def outer_master():
    a=10
    b=23
    print(a,b)
    def outer():
        nonlocal a,b
        a+=10
        b-=12
        print(a,b)
        def inner():
            nonlocal a,b
            a,b=b,a
            print(a,b)
        inner()
        print(a,b)
    outer()
    print(a,b)
outer_master()

