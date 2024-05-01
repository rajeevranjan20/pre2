a=int(input("Enter the value of a:"))
r=int(input("Enter the common ratio:"))
n=int(input("Enter the value of n:"))
sum=0
for x in range(0,n+1):
    sum=a*r**x +sum
print(sum)    