n=int(input("Enter number: "))
temp=n
sum=0
a=10
while(n>0):
    n1=n%a
    sum=sum*10+n1
    n=n/a
if(temp==sum):
    print(n," is palindrome!")
else:
    print(n," is not palindrome!")
