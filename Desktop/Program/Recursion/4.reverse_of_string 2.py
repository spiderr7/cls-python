def sample(string,n):
    if n==0:
	    return
    print(string[n-1],end="")
    sample(string,n-1)
sample("MEOW",len("MEOW"))
