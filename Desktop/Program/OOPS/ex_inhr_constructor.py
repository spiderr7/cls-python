class A:
    a=10
    b=20
    def __init__(self,p):
        print("Construtor of Parent class")
        self.p=p

class B(A):
    c=30
    d=40
    def __init__(self,p,q):
        print("Construtor of Child class")
        self.p=p
        self.q=q

oa=A(1)
ob=B(2,3)

print(oa.p)
print(ob.p,ob.q)
