# convert uppercase into lowercase and lower to upper

c=input("Enter The Alphabet Character:")
a=ord(c)
res= chr(a+32) if 65<=a<=90 else chr(a-32) if 97<=a<=125 else f'"Invalid"'
print(res)