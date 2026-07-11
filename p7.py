def fun(n,default_v="Null"):#if no value parameterized to default_v, then Null will be printed
    print(f"{n}*10 = {n*10}")
    print(default_v)
    return "variable"
n=int(input("Enter the number: "))
res=fun(n,5)
print(res)
fun(n)
fun(10,"Done")  
def sum(name,def_v):
    print("Earth"+ "Mother"+name)
    print(def_v)
    return 0
print(sum("Done",1))
# noqa: F821
