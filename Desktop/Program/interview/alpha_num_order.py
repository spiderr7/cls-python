s="zxgjr45ZXCJKyua9186"
temp1=[]
temp2=[]

for i in s:
    if i>='a' and i<='z' or i>='A' and i<='Z':
        temp1.append(i)

        
    elif i>='0' and i<='9':
        temp2.append(i)
        
temp1.sort()
print(temp1)

temp2.sort()
print(temp2)

temp=" ".join(temp1+temp2)
print(temp)
