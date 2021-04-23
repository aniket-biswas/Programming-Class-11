#1
a=int(input("Enter No:"))
b=int(input("Enter No:"))
c=int(input("Enter No:"))
list=[a,b,c]
for i in range(0,len(list)):
    print(list[i])
#2
list=["A","B","c",1,2]
print(list[0:3])

#3
list=['d']
list.append("A")
print(list)

#4
list=[4,5,6]
list.extend([7,8,9])
print(list)

#5
fruits=["Apple","Banana"]
cars=["SUV","Sedan"]
fruits.extend(cars)
print(fruits)

#6
l1=[1,2,3]
l2=[4,5,6]
print(l1+l2)

#7
l3=[7,8,9]
del l3[1]    # We have to write the index of the element that we want to delete
print(l3)

#8
a=  [1,2,3]     # Membership Check
print(5in a)

#9
for x in[8,9,10,11]:    # Iteartion
    print(x)

#10
a=[7,8,9,10,11,12,13]
a.insert(4,"Ma'am")      #insert=> first index than  element
print(a)

#11
b=[1,2,3,4,5,6]
b.pop(1)     #pop() removes the element in the given index
print(b)

#12
c=["Aniket","School","DPS"]
c.sort()        #sort() displays the list in  order it's inbuilt value is Ascending Order
print(c)

#13
d=["Aniket","School","DPS","North"]
d.reverse()        #reverse=> reverses the list
print(d)

#14
d=["Aniket","Biswas","Class",11]
print(len(d))

#15
d=["Aniket","Biswas"]
print(max(d))         #Checks ASCII value of the first index of the string
print(min(d))

#16
d=[16,17,18]
print(max(d))        #Checks the value
print(min(d))

#17
d=[16,17,18,19,20,20,21,21]
a=tuple(d)                   #Conversion of one data type to other  --tuple
b=set(d)                      #Conversion of one data type to other  --set
print(a)
print(b)

#18
kk="Aniket Biswas"
c=list(kk)                 #String to list
print(c)

#19
j="Anikettt Biswasss"
a=j.count("a")                #counts the no of character in the data type which is given under parenthesis
b=j.count("s")
print(a)
print(b)

#20
a=[]
n=int(input("Enter number of elements:"))
for i in range(1,n+1):
        b=int(input("Enter Element:"))       #Finding largest/Maximum No using sort()
        a.append(b)
a.sort()
print("Largest Element is:",a[n-1])






























