num=int(input("Enter the Number:"))
x=int(input("Enter the value of x:"))
fact=1
rst=1
for i in range(1,num+1):
    
    fact=fact*i
    rst= rst+(x**i)/fact
print(rst)