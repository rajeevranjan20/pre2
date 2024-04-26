#program to calculate eletricity bill
n=eval(input("Enter the number of Unit:"))
if n<=100:
    print("No Bill")
elif 100<n<=200:
    amt=(n-100)*5
    print(f'Bill Amount:{amt}')
else:
    n1=n-200
    amt1=n1*10+100*5
    print(f'Bill Amount:{amt1}')
