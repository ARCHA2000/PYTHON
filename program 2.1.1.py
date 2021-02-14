n=int(input("enter a number:"))
fact=1
if(n<0):
    print("factorial not found for negative number:")
elif(n==0):
    print("factorial of zero is:",fact)

else:
    for i in range(1,n+1):
        fact=fact*i
    print("factorial of",n,"is",fact)
