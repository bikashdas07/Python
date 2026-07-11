import math
print("Enter three sides of the triangle")
s1=int(input())
s2=int(input())
s3=int(input())
s=((s1+s2+s3)/2)
area= (math.sqrt(s*(s-s1)*(s-s2)*(s-s3)))
print("Area of the triangle is: ",area)