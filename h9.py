num=int(input("Enter the number:"))
sum=0
temp=num
for x in  range (1,num):
    if num%x==0:
        sum=x+sum
    else:
        pass    
if temp==sum:
    print("Perfect Number")
else:
    print("Not Perfect Number")
     