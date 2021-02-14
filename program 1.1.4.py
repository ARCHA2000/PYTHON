year=int(input("enter year"))
total_years = int(input("enter year limit:"))
i=year
while(i<total_years):
    if (i % 4) == 0 or (i % 400) == 0 and (i % 100) == 0:
        print(i)
    i=i+1
