#find input character is albhabeyt, digit or special

c=input("Enter the Character:")
a=ord(c)
res=f'{c} is Alphabet' if 65<=a<=122 else f'{c} is Digit' if 48<=a<=57 else f'{c} is Special Character'
print(res)