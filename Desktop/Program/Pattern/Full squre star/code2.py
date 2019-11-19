n=20
k=1
for j in range(1,n+1):
    for i in range(1,n+1):
        if i+j<=n+1 and i<=j or i+j>=n+1 and i>=j:
            print("*",end="")
        else:
            print(" ",end="")
    print()


