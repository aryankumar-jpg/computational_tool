
def calfact(n):
    if n<0:
       print("factorial not valid")
    elif n==0 or n==1:
        print(1)
    else:
        factorial=1
        for i in range(2,n+1):
            factorial*=i
        print(factorial) 

#jhgjgghg
def prime(inp):
    if inp<=1:
        print("not prime")
        return
    is_p = True
    for i in range(2, int(inp**0.5) + 1):
        if inp % i == 0:
            print("not a prime")
            is_p=False
            break
    if is_p:
            print("prime")
   



n=int(input("enter an integer: "))
calfact(n)
prime(n)
      
