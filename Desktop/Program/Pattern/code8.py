#ALPHABET
print("NOTE 5")
print("ALPHABET")
print("COUNT n")
n=5
k= ord('A')
for j in range (1,n+1):
    for i in range (1,n+1):
        if i<=j:
            print(chr(k),end=" ")
            k+=1
        else:
            print(" ",end=" ")
    print()
print("-"*50)

k= ord('A')
for j in range (1,n+1):
    for i in range (1,n+1):
        if i>=j:
            print(chr(k),end=" ")
            k+=1
        else:
            print(" ",end=" ")
    print()
print("-"*50)
print("-"*50)

#NUMBER
print("NUMBER")
print("COUNT n")
k=1
for j in range (1,n+1):
    for i in range (1,n+1):
        if i<=j:
            print(k,end=" ")
            k+=1
        else:
            print(" ",end=" ")
    print()
print("-"*50)

k=1
for j in range (1,n+1):
    for i in range (1,n+1):
        if i>=j:
            print(k,end=" ")
            k+=1
        else:
            print(" ",end=" ")
    print()
print("-"*50)
