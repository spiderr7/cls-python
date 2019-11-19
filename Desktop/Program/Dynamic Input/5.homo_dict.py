#DICT

def input_homo_dict(n):
    temp={}
    for i in range(n):
        key=input("Enter the key : ")
        value=int(input("Enter the value : "))
        temp[key]=(value)
    return temp
n=int(input("Enter the no. of element of Dict : "))
dict_value=input_homo_dict(n)
print(dict_value)


#OUTPUT:
"""
Enter the no. of element of Dict : 5
Enter the key : a
Enter the value : 1
Enter the key : b
Enter the value : 2
Enter the key : c
Enter the value : 3
Enter the key : d
Enter the value : 4
Enter the key : e
Enter the value : 5
{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

"""
