n=int(input("enter a number"))
def fib(n):
    a=0
    b=1
    while a<n:
        print(a)
        a,b=b,a+b
fib(n)
    
