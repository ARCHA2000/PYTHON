d={'beautiful':3,'flower':5,'a':2}
print("the dict is:\n",d)
li1=list(d.items())
li1.sort()
print("list in ascending order:\n",li1)
li2=list(d.items())
li2.sort(reverse=True)
print("list in descending order:\n",li2)
