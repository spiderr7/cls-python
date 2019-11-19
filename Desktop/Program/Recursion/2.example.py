def sample(n):
    print(n,end="")
    if(n==0):
        return
    sample(n-1)
    print(n,end="")
sample(5)
