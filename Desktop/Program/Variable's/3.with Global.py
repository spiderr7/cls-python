#WITH GLOBAL
a=[1,2,3,4]
print(a)
def app():
    global a
    a=10
    
app()
print(a)
