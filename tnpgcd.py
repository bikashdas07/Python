a=int(input("Enter the 1st number: "))
b=int(input("Enter the 2nd number: "))
if(a<b):
    min=a
else:
    min=b
for i in range (1,min):
    gcd=0
    if(a%i==0 && b%i==0):
        gcd=i
        continue
print("gcd of the given numbers are: ",gcd)
