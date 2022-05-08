import sys
a=0
b=1
c=0
try:
    print("Enter The Limit :")
    n=int(input(sys.argv))
    if(n>=1):
        sys.argv.append(0)
    if(n>=2):
        sys.argv.append(1)
    for i in range(2,n):
        c=a+b
        sys.argv.append(c)
        a=b
        b=c      
except ValueError:
    print("Enter an integer")
except NameError:
    print("Enter an integer")
#if the user needs fib series upto 

print(sys.argv)
