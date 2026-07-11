def pattern():
    if (n==0):
        return 
    print("*"*n)
    pattern(n-1)
    pattern(8)

def fact(n):
    if(n==0 or n==1): 
        return 1
    return n * fact((n-1))
        
n=int(input("Enter a number: "))
print(f"Factorial is {fact(n)}") 

def celfer(f):
    return 5*((f-32)/9) 
def fercel(c):
    return (c*9/5)+32
c=int (input("Enter the temperature in celcius: "))
f=int (input("Enter the temperature in ferhenite: "))
cel = celfer(c)
print(f"Equivalent celcius is {round (cel,2)}")
fer = fercel(f)
print(f"Equivalent Farhenite is {round (fer,2)}")
