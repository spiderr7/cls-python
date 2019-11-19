def unpacking(a,b,c):
    print("a:",a,end="|")
    print("b:",b,end="|")
    print("c:",c)
    print("-"*50)
a="Hai"
b=[1,2,3]
c=(4,5,6)
d={7,8,9}
e={'a':1,'b':2,'c':3}
unpacking(*a)
unpacking(*b)
unpacking(*c)
unpacking(*d)
unpacking(*e)
unpacking(**e)
