#singleton

def singleton(cls):
    instances={} #maintion class_name and object address
    def inner(*args,**kwargs):
        if cls not in instances:
            obj=cls(*args,**kwargs)
            instances[cls]=obj
        return instances[cls]
    return inner
@singleton
class A:
    def __init__(self,a):
        self.a=a
        print("object creation")

oa=A(55)
ob=A(66)
oc=A(77)
print(oa,oa.a)
print(ob,ob.a)
print(oc,oc.a)
