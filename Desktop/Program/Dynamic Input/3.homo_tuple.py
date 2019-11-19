#TUPLES

def input_homo_tuple(n):
    temp=[]
    for i in range(n):
        value=int(input("Enter the value : "))
        temp.append(value)
    return tuple(temp)
n=int(input("Enter the no. of element of list : "))
tuple_value=input_homo_tuple(n)
print(tuple_value)


#OUTPUT:

"""
Enter the no. of element of list : 5
Enter the value : 1
Enter the value : 2
Enter the value : 3
Enter the value : 4
Enter the value : 5
(1, 2, 3, 4, 5)

"""
