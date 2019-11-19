
# 1.For Number
print("NOTE 1")
print("1.For Number")
n=5
for j in range(1,n+1):
    k=1
    for i in range(1,n+1):
        if i<=j:
            print(k,end=" ")
            k+=1
        else:
            print(" ",end=" ")    
    print()

print("-"*50)


for j in range(1,n+1):
    k=1
    for i in range(1,n+1):
        if i>=j:
            print(k,end=" ")
            k+=1
        else:
            print(" ",end=" ") 
    print()
    
print("-"*50)


