#1st for key and 2nd time for values and keys(two stars)

def packing(**var):
    print(*var)
    print(var)
    print(type(var))
    print("-"*50)
packing()
packing(x=10)
packing(y=20,z=30)
packing(a=10,b=20,c=30,d=40,e=50)
