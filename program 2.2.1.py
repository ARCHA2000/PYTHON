def _ing(str1):
    if(len(str1)>=3):
        if(str1[-3:]=='ing'):
            str1=str1+"ly";
        else:
            str1=str1+"ing"
    print("modified string:",str1)
str=input("enter a string:")
_ing(str)
