
# 2.For Alphabet
print("NOTE 1")
print("2.For Alphabet")
n=5
for j in range(1,n+1):
    k= ord('A')
    for i in range(1,n+1):
        if i<=j:
            print(chr(k),end=" ")
            k+=1
        else:
            print(" ",end=" ")    
    print()

print("-"*50)


for j in range(1,n+1):
    k= ord('A')
    for i in range(1,n+1):
        if i>=j:
            print(chr(k),end=" ")
            k+=1
        else:
            print(" ",end=" ") 
    print()

print("-"*50)
