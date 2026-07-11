# If-elif-else-ladder
a=int(input("Enter the  Day number:"))
if a==1:
    print("Monday")
elif a==2:
    print("Tuesday")
elif a==3:
    print("Wednesday")
elif a==4:
    print("Thursday")
elif a==5:
    print("Friday")
elif a==6:
    print("Saturday")
elif a==7:
    print("Sunday")
else:
    print("Invalid input") 
n=int(input("Enter the number:"))
# Another if statement without else
if n>0:
    print("Positive number")
marks1=int(input("Enter your marks1 o/of 100: "))
marks2=int(input("Enter your marks2 o/of 100: "))
marks3=int(input("Enter your marks3 o/of 100: "))    
total_percentage=(100*(marks1+marks2+marks3))/300
if(total_percentage>40 & marks1>=33 and marks2>=33 & marks3>=33):
    print("you are pased!",total_percentage)
else:
    print("You are fail$",total_percentage)
    