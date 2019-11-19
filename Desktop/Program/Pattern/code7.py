#ALPHABET
print("NOTE 4")
print("ALPHABET")
print("REVERSE")
n=5
for j in range (1,n+1):
    k= ord('A')+n-j
    for i in range (1,n+1):
        if i>=j:
            print(chr(k),end=" ")
            k-=1
        else:
            print(" ",end=" ")
    print()
print("-"*50)
print("-"*50)

print("NUMBER")
print("REVERSE")
for j in range (1,n+1):
    k= 1+n-j
    for i in range (1,n+1):
        if i>=j:
            print(k,end=" ")
            k-=1
        else:
            print(" ",end=" ")
    print()
print("-"*50)
