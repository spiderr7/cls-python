#NUMBER
print("NUMBER")
print("[%2!=0]")
n=5
k=1
for j in range (1,n+1):
    l=k+j-1
    for i in range (1,n+1):
        if i<=j:
            if (j%2!=0):
                print(k,end=" ")
            else:
                print(l,end=" ")
                l-=1
            k+=1
        else:
            print(" ",end=" ")
    print()
print("-"*50)
print("-"*50)

#ALPHABET
print("ALPHABET")
print("[%2!=0]")
k= ord('A')
for j in range (1,n+1):
    l=k+j-1
    for i in range (1,n+1):
        if i<=j:
            if (j%2!=0):
                print(chr(k),end=" ")
            else:
                print(l,end=" ")
                l-=1
            k+=1
        else:
            print(" ",end=" ")
    print()
print("-"*50)
