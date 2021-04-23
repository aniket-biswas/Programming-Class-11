d={"Aniket":"Biswas","Class":11,"School":"DPS"}
print(d)
print(d.values()) #Gives the values
print(d.keys())       #Gives the keys
print(d["Aniket"])    #Gives the value
print(len(d))         #Gives the length of pair
print(d.get("Class")) #Gives the value of the key
print(d["School"])
for i in d:
    print(i , d[i])    #i will print the keys and d[i] will print the values
d["Class"]="XI A"      #updating/editing the dictionary left side == key & right side the updated element
print(len(d))
print(str(d))
print(type(d))
print(d["Class"])
del d["Aniket"]
print(d)
d.pop("School")
print(d)
x=dict(name="Aniket",clas="11")
print(x)
print(x.values())
print(x.keys())








