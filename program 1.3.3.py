n1=float(input("enter the first number:"))
n2=float(input("enter the second number:"))
n3=float(input("enter the third number:"))
big=0
if(n1>n2)and(n1>n3):
    big=n1
elif(n2>n1)and(n2>n3):
    big=n2
else:
    big=n3
print("largest number is:",big)
