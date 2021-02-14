list=[]
n=int(input("enter the number of element:"))
for i in range(0,n):
    num=int(input("enter number"))
    if num>100:
        list.append("over")
    else:
        list.append(num)
print(list)
