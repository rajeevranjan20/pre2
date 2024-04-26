#display last digit
n=int(input("Enter the Number:"))
if n<10:
    print(f'Last digit of number:{n}')
else:
    l=n%10
    print(f'Last digit of number:{l}')