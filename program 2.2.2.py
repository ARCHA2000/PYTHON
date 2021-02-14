def long(list):
    max=0
    for i in list:
        if(len(i)>max):
            max=len(i)
            temp=i
        print("word with longest length:",temp,"=",max)

list=["flowers","vegetables","fruits"]
long(list)
