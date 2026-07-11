#Bouncers
a=1
b=100
print(a+b)
print("a is greater than b", a>b)
c=input("Enter the number:" )
d=input("Enter another number: ")
print(c+d)#"cd concatenate"
print("c is greater than d", c>d)
s=set()
s.add(1)
s.add(1.0)
s.add('1')
print(s)
print(len(s))
dict={}
for i in range(4):
    key=input("Enter name:")
    value=input("Enter age:")
    dict.update({key:value})
print(dict)
#in k.w. use
t1="money"
t2="Sunny day"
t3='Simulation'
mes=input("Enter your message: ")
if(t1 in mes or t2 in mes or t3 in mes):
    print("Its for us!")
else:
    print("Go ahead!")
if("sunny" in t2.lower()):#user input()
    print("This is about sun.")
