#leap year

y=int(input("Enter the Year:"))
res=f'{y} is leap year' if ( y % 4 == 0 and y % 100 != 0 ) or ( y % 400 == 0 ) else f'{y} is not a leap Year '
print(res)