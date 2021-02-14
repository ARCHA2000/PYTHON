list = [1,2,3,4,5,6]
print("Original list:",list)
for i in list:
    if(i%2 == 0):
        list.remove(i)
print('list after removing EVEN numbers:",list)
