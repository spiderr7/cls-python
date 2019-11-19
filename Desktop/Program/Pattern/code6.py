#ALPHABET
print("NOTE 3")
print("ALPHABET")
print("FORWORD BY DECREASE")
n=5
for j in range (1,n+1):
    k= ord('A')+n-1
    for i in range (1,n+1):
        if i<=j:
            print(chr(k),end=" ")
            k-=1
        else:
            print(" ",end=" ")
    print()
print("-"*50)


for j in range (1,n+1):
    k= ord('A')+n-1
    for i in range (1,n+1):
        if i>=j:
            print(chr(k),end=" ")
            k-=1
        else:
            print(" ",end=" ")
    print()
print("-"*50)
print("-"*50)

#NUMBER
print("NUMBER")
print("FORWORD BY DECREASE")
for j in range (1,n+1):
    k= 1+n-1
    for i in range (1,n+1):
        if i<=j:
            print(k,end=" ")
            k-=1
        else:
            print(" ",end=" ")
    print()
print("-"*50)


for j in range (1,n+1):
    k= 1+n-1
    for i in range (1,n+1):
        if i>=j:
            print(k,end=" ")
            k-=1
        else:
            print(" ",end=" ")
    print()
print("-"*50)


    
