class A:
    a=10

    def __init__(self,b):
        self.b=b

class B(A):
    c=12

    def __init__(self,b,c):
        super(B,self).__init__(b)
        self.c=c

    def __AddElement(self,d):
         self.d=d
  
    @classmethod
    def get_call__AddElement(cls,self,d):
        cls.__AddElement(self.d)

oa=A(10)
ob=B(20,30)
#B.__AddElement(oa,13)

B.get_call__AddElement(oa,15)
