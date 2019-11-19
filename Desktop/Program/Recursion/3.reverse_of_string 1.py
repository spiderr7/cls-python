def sample(string,n):
    if (n==0):
        return ""
    return string[n-1]+ sample(string,n-1)
rstr=sample("utkarsh",len("utkarsh"))
print(rstr)
