# road tax
b=eval(input("Enter the cost of Bike:"))
if b>100000:
    tax=b*0.15
    print(f'Tax Paid {tax}')
elif 50000<b<=100000:
    tax=b*0.1
    print(f'Tax Paid {tax}')
else:
    tax=b*0.05
    print(f'Tax Paid {tax}')