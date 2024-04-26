#leap year
y=int(input("Enter the Year:"))
if (y%4==0 and y!=100)or y%400==0:
    print(f'{y} is Leap Year')
else:
    print("Not Leap Year")