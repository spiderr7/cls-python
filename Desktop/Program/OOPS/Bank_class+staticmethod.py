class Bank:
    B_name="ICICI"
    ROI=14/100
    MBL="Mumbai"

    def __init__(self,Name,Age,Phno,Bal=0):
        self.Name=Name
        self.Age=Age
        self.Phno=Phno
        self.Bal=Bal
        
    def display(self):
        print("Name is:",self.Name)
        print("Age is:",self.Age)
        print("Phno is:",self.Phno)
        print("Balance is:",self.Bal)

    def deposit(self,amt=0):
        if amt==0:
            amt=self.get_amount()
        self.Bal=self.add(self.Bal,amt)
        print("Amount is deposited successfully")
        return self.Bal

    def withdraw(self,amt=0):
        if amt==0:
            amt=self.get_amount()
        if self.Bal>=amt:
            self.Bal=self.sub(self.Bal,amt)
            print("Withdraw Successfully")
        else:
            print("Insufficent Balance")
            print(self.Bal)

@classmethod
def Modify_ROI(cls,New_ROI):
    cls.ROI=New_ROI
    print("Rate intrest is been changed to",cls.ROI)

@classmethod
def Modify_Bank_name(cls,New_name):
    cls.B_name=New_name
    print("Changed accepted and the bank name is",cls.B_name)

@classmethod
def Disp_cls_data(cls):
    print("Modification is happening in",cls)
    print("Name of Bank is",cls.B_name)
    print("Rate of Interest is",cls.ROI)
    print("Main Branch Location is",cls.MBL)

@staticmethod
def get_amount():
    amount=float(input("Enter amount:"))
    return amount

@staticmethod
def add(a,b):
    return a+b

@staticmethod
def sub(a,b):
    return a-b

@staticmethod
def get_ROI():
    roi=float(input("Enter the new rate of interest:"))
    return roi

Dinga=Bank("Dinga",31,9123123123,10000)
Dingi=Bank("Dingi",28,9321321321)


















    
        
