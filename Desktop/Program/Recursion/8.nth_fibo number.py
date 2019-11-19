def nth_fibo(n):
    fib1=0
    fib2=1
    for i in range(3,n+1):
        fib=fib1+fib2
        fib1,fib2=fib2,fib
    return fib
print(nth_fibo(8))
