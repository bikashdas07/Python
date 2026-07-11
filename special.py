n=int(input("Enter the number: "))
temp=n
sum=0
while (n>0):
    rem=int(n%10)
    n=n/10
    fact=1
    for i in range(1,rem):
        fact=fact*i
    sum=sum+fact
if(sum==temp):
    print("The number is special.")
else:
    print("The number is not special.")   