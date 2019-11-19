class A:
    a=10
    b=20

class B(A):
    c=30
    d=40

oa=A()
ob=B()

print(A.a,A.b)
print(oa.a,oa.b)
print(B.a,B.b,B.c,B.d)
print(ob.a,ob.b,ob.c,ob.d)

print("Modification wrt to PARENT class.")

A.a=15
print(A.a,A.b)
print(oa.a,oa.b)
print(B.a,B.b,B.c,B.d)
print(ob.a,ob.b,ob.c,ob.d)

print("Modification wrt to CHILD class.")

B.c=45
print(A.a,A.b)
print(oa.a,oa.b)
print(B.a,B.b,B.c,B.d)
print(ob.a,ob.b,ob.c,ob.d)
