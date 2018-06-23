from math import *
n= int(input("Enter a number to check all"))

print("You have entered : %d" %n)


def isFib(n):
    print("Checking for Fibonacci number...................")
    if(n>0):
        n1= (5*n*n)+4
        n2= (5*n*n)-4
        sn1=n1**(1/2)
        sn2= n2**(1/2)
        sn1=round(sn1,2)
        sn2= round(sn2,2)
        if(sn1*sn1==n1 or sn2*sn2==n2):
            print("%d is a fibonacci number"%n)
        else:
            print("%d is a not fibonacci number"%n)



    else:
        print("%d is not a fibonacci number" %n)

def isPerfectSq(n):
    print("Checking for perfect square..................")
    n1=n**(0.5)
    n1=round(n1,2)
    if(n1*n1==n):
        print("%d is a perfect square"%n)
    else:
        print("%d is not a perfect square "%n)


def isPrime(n):
    print("Checking for prime number..............")
    if(n>0):
        if(n==2):
            print("%d is a prime number, only even prime "%n)
        else:

            for i in range(2,n):
                if(n%i==0):
                    print("%d is not a prime number"%n)
                    break
            else:
                print("%d is a prime number.."%n)

    else:
        print("%d is not a prime square "%n)


isPrime(n)
isPerfectSq(n)
isFib(n)

