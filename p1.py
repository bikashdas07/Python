#String"IMMUTABLE"
str= "Hopediamond"
print(str)
print(str.sort())
str1=' '
print(str1,type(str1))
print(str[0:6:2])
#List[MUTABLE]
li=[1,"Radhe","ayu",2.5,True]
print(li)
print(type(li))
if("ayu" in li ):#or can take user i/p./
    print("you are!")
li1=[]#empty list
print(li1,type(li1))

#Tuple(IMMUTABLE)
tup=(1,2,3)
print(tup)
empty_tup=()#empty tuple
print(empty_tup,type(empty_tup))
tup1=(1,)#exceptional
print(tup1)

#Dictionary{MUTABLE}
dict={'1':"Harry",
    "honey":"Rohini",
    1:"Ram" ,
    "Ice":29,
    "list":[1,2,3]
    } #in key value pairs
print(dict,type(dict))  
dict1={} #empty dictionary
print(dict1,type(dict1))
print(dict["honey"],[1]) #if key isn't present, returns error
print(dict)
print(dict.keys())
print(dict.values()) 
dict.update({"Ice":"30",'ice':45})
print(dict.values())
print(dict.get(1))#if key doesn't exist in dictionary, prints NONE
v=dict.pop("ice")#delete the specified key and returns its value.
print(v)
print(dict.keys())
item=dict.popitem()#deletes last item from the dictionary.
print(item)
print(dict)
d=input("Enter the key:")
print(dict[d])#prints the value of the key.


#set, Collection of well defined objects.#Not accessible by index
s={1,2,32,445,5,5,5,7,7,4.5,4.5,"Make"}
print(s,type(s))#No repetition#unordered
s1=set()#empty set
print(s1,type(s1))
s.add(9)
print(len(s))
s.remove(1) 
#s.clear() remove all the elements
print(s)
s2={2,32,6,8}
s5={2,6}#subset of s2
print(s.union(s2))#all values (i.e. not repeating)
s3={2,32,3}
print(s2-s3)#set operation
print(s5.issubset(s2))
print(s2.issuperset(s5))