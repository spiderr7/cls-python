class A:
    a=10
    _a=100
    __a=1000

    def __init__(self,b,c,d):
        self.b=b
        self._b=c
        self.__b=d

    def get(self):
        return self.__b

    def set(self,value):
        self.__b=value

    def disp(self):
        print(self.b,self._b,self.__b)

    @classmethod
    def get_cls(cls):
        return cls.__a

    @classmethod
    def set_cls(cls,value):
        cls.__a=value

    @classmethod
    def display(cls):
        print(cls.a,cls._a,cls.__a)

A.display()
oa=A(10,20,30)
oa.disp()
print(oa.get())
oa.set(40)
print(oa.get())
print(oa.get_cls())
A.set_cls(1001)
print(A.get_cls())
