
#ALPHABET FORWORD
print("NOTE 2")
print("ALPHABET FORWORD")
n=5
for j in range (1,n+1):
    k= ord('A')+j-1
    for i in range (1,n+1):
        if i<=j:
            print(chr(k),end=" ")
            k+=1
        else:
            print(" ",end=" ")
    print()
print("-"*50)

#ALPHABET REVERSE
for j in range (1,n+1):
    k= ord('A')+j-1
    for i in range (1,n+1):
        if i>=j:
            print(chr(k),end=" ")
            k+=1
        else:
            print(" ",end=" ")
    print()
print("-"*50)
print("-"*50)

#NUMBER FORWORD
print("NUMBER FORWORD")
for j in range (1,n+1):
    k= 1+j-1
    for i in range (1,n+1):
        if i<=j:
            print(k,end=" ")
            k+=1
        else:
            print(" ",end=" ")
    print()
print("-"*50)

#NUMBER REVERSE
for j in range (1,n+1):
    k= 1+j-1
    for i in range (1,n+1):
        if i>=j:
            print(k,end=" ")
            k+=1
        else:
            print(" ",end=" ")
    print()
print("-"*50)


        
        

        
