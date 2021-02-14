f=0
s=1
n=int(input("enter the limit:"))
print("series are:")
print(f)
print(s)
for i in range(1,n):
    t=f+s
    f=s
    s=t
    print(t)
