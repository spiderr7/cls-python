def packing(*var):
    print(*var)
    print(var)
    print(type(var))
    print("-"*50)
packing()
packing(10)
packing(10,20)
packing(10,20,30,40,50)
