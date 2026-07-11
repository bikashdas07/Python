def factorial(n):
    c=1
    for i in range(1,n+1):
        c=i*c
    return (c)
n1=int(input ("Enter a number greater than 0 to find its factorial: "))
fact=factorial(n1)
print ("The factorial is: ",fact)