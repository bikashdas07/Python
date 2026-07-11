x=10 #global variable
def main():
    global x
    x=x+1
    global y#local for main
    y=x+10
    print("Main function")
    print("global x",x)
    print(y)
def insider()
    x=100
    x=x+2
    global y#global for insider
    y=x+y
    print("I am insider function")
    print("local x",x)
    print(y)
main()
insider()   
print("global x",x) 

