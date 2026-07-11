li=[1,"Biki","Money",'India']
i=0
while(i<len(li)):#condition should eventually false.
    print(li[i]) #Execution 
    i+=1 #iteration

for i in range(4):
    print(li[i]) 

str="Comeback"
for i in str:
    print(i)

t1=(2,"B",'a',43)
for i in t1:
    print(i)
else:
    print("End")
 
for i in range(0,100,5):
    if(i==95):
        break #exit the loop.
    if(i==55):
        continue #skip the iteration
    print(i) 

for i in range(10):
    pass #if not used then indentation error will occur and next while loop can't be executed.
        #To skip the loop , opted for further using.
i=0
while(i<4):
    print(i)
    i+=1

n=int(input("Enter the table number: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")

l=["Raj","Rakesh","Sanu"]
for name in l:
    if(name.startswith("R")):
        print("Hello",name)
        # print(f"Hello {name}")
no=int(input("Enter a number: "))
if (no==1 or no==0):
    print(f"{no} is neither prime nor composite.")
else:
    for i in range(2,no):
        if(no%i==0):
            print(f"{no} is not prime.")
            break
    else:
        print(f"{no} is prime.")
f=int(input("Enter the number to find its factorial: "))
fact=1
for i in range(1,f+1):
    fact=fact*i
print(f"The factorial of {f} is {fact}")
for i in range(1,101):
    if(i%3==0 and i%5==0):
        print("FizzBuzz")
    elif(i%3==0):
        print("Fizz")
    elif(i%5==0):
        print("Buzz")
    else:
        print(i)
n=int(input("Enter the number: "))
for i in range(1,n+1):
    print(" "*(n-i))
    print("*"*i)