class A:
    __a=10

    def __init__(self,b):
        self.__b=b

class B(A):
    c=12

    def __init__(self,b,c):
        super(B,self).__init__(b)
        self.c=c

    def display(self):
        print(self._A__b) #("by it we can call private variable")

    def __AddElement(self,d):
        self.d=d

    @classmethod
    def get_call__AddElement(cls,self,d):
        cls.__AddElement(self,d)
        

oa=A(12)
ob=B(33,22)
ob._B__AddElement(15)
ob.display()
print(oa._A__b)
        
