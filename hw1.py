#find input number is -ve,+ve or 0

num=int(input("Enter the number:"))
res=f'{num} is Positive' if num>0 else f'{num} is Negative' if num<0 else f'{num} is Zero'
print(res)