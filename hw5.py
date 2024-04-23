#find max of two number

num1=int(input("Enter the first Num:"))
num2=int(input("Enter the second Num:"))
res=f'{num1} is max' if num1>num2 else f'{num2} is max' if num1<num2 else f'{num1,num2} is Equal'
print(res)