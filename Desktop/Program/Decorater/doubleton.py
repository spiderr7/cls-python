#DoubleTon

def doubleton(cls):
    instances={}
    flag=0
    def inner(*args,**kwargs):
        nonlocal flag
        if cls not in instances:
            instances[cls]=[]
        if len(instances[cls])<2:
            obj=cls(*args,**kwargs)
            instances[cls].append(obj)
        elif flag==0:
            obj=instances[cls][0]
            flag=1
        else:
            obj=instances[cls][1]
            flag=0
        return obj
    return inner

@doubleton
class A:
    def __init__(self,a):
        self.a=a
        print("Object Creation")

oa=A(12)
ob=A(15)
oc=A(19)
od=A(22)
print(oa,oa.a)
print(ob,ob.a)
print(oc,oc.a)
print(od,od.a)
