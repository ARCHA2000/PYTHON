list1=[1,2,3,4,5]
list2=[6,7,4,10]
x=len(list1)
y=len(list2)
if(x==y):
    print("length are same:")
else:
    print("length are not same:")
a=sum(list1)
b=sum(list2)
if(a==b):
    print("sum are same:")

else:
    print("sum are not same")
value=any(check in list2 for check in list1)
print("common value",value)
print(set(list2).intersection(set(list1)))
