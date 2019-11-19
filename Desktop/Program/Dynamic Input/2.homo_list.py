#LIST

def input_homo_list(n):
    temp=[]
    for i in range(n):
        value=int(input("Enter the value : "))
        temp.append(value)
    return temp
n=int(input("Enter the no. of element of list : "))
list_value=input_homo_list(n)
print(list_value)

#OUTPUT:
"""
Enter the no. of element of list : 5
Enter the value : 1
Enter the value : 2
Enter the value : 3
Enter the value : 4
Enter the value : 5
[1, 2, 3, 4, 5]

"""
