#SET

def input_homo_set(n):
    temp=set()
    for i in range(n):
        value=int(input("Enter the value : "))
        temp.add(value)
    return tuple(temp)
n=int(input("Enter the no. of element of Set : "))
set_value=input_homo_set(n)
print(set_value)


#OUTPUT:
"""
Enter the no. of element of Set : 5
Enter the value : 1
Enter the value : 1
Enter the value : 2
Enter the value : 2
Enter the value : 3
(1, 2, 3)
"""
