name='''Tim'''
age=False
height=None
print(type(name))
print(type(age))
print(type(height))
A=1.5
B=3
print(A//B)
a=int(input("Enter 1st number: "))
b=float(input("enter 2nd number: "))
print(a+b)
ag=int(input("Enter your age: "))
if(ag==18):
    print("you are 18")
elif(ag>18):
    print("you are aged")
elif(ag>18):
    print("you are young")
else:
    print("Invalid Input")
number=int(input("Enter a number: "))
print("Okay" if number== 10 else "Not okay")
data=float(input("Enter your used data in Mb: "))
d=("Finished" , "not-finished") [data<1024]
print(d)
#type conversion
a=2
b=4.25
print(a+b) #Integer will automatically convert into float by the enterpreter
#type casting
a=int("2") #Explicitly we are converting string into integer
b=4.3
print(a+b)
