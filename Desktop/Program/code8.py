a=[]
for i in range(1,20):
    for j in range(1,20):
        for k in range(1,20):
            if(i*i+j*j)==(k*k):
                a.append((i,j,k))
print(a)
