def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1) + fib(n-2)


def series(t):
    if t<=0:
        print("enter positive number")
    else:
        print(f"fib series upto {t} terms")
        for i in range(t):
            print(fib(i),end=" ")

n=int(input("enter an integer: "))
series(n)
   