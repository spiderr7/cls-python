# 1.[if i>=j]
print("CODE TO PRINT STAR(*)")
print("[if i>=j]")
n=5
for j in range(1,n+1):
    for i in range(1,n+1):
        if i>=j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
print("-"*50)

# 2.[if i==j]
print("[if i==j]")
for j in range(1,n+1):
    for i in range(1,n+1):
        if i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
print("-"*50)
print("[if i<=j]")
# 3.[if i<=j]
for j in range(1,n+1):
    for i in range(1,n+1):
        if i<=j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
print("-"*50)

