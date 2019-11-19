

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def get_elements():
    a=int(input("Enter the value for A : "))
    b=int(input("Enter the value for B :"))
    return a,b

def cal():
    ch=input("1.Addition 2.Subtraction 3.Nothing")
    
    
    if ch=='1':
        a,b=get_elements()
        res=add(a,b)
    elif ch=='2':
        a,b=get_elements()
        res=sub(a,b)
    else:
        print("Invalid Input")
        res=0
    
    print(res)
    
cal()
