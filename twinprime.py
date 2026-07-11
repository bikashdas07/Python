def twinprime(n) :
       c=0
       for i in range (2,n):
               if (n%i==0):
                     c=c+1
       return (c)
n1=int(input ("Enter a number"))
n2=int(input ("Enter a number"))
x=twinprime(n1)
y=twinprime (n2)
if (x==0) and (y==0) and (n1-n2 ==2) or (n1-n2 ==-2) :
         print ("Twin prime number")
else :
         print ("Not a twin prime")