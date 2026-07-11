n = int(input("Enter the number: "))
temp = n
s = 0
count = 0
while (n > 0):
    count = count+1
    n = n/10
while (n > 0):
    rem = int(n % 10)
    x = pow(rem, count)
    s = s+x
    count = count-1
    n = n/10
if (s == temp):
    print("The number is Disarium.")
else:
    print("The number is not Disarium.")
