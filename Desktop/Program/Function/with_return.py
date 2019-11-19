#WITH RETURN
a,b=1,2
print(a,b)
def get_data():
    a=10
    b=20
    print(a,b)
    return a,b
a,b=get_data()
print(a,b)
