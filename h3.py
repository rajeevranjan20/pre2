#last digit of number divisible by 3
n=int(input("Enter the number:"))
l=n%10
if l%3==0:
    print(f'Last Digit divisible by 3')
else:
    print("Not Divisible by 3")