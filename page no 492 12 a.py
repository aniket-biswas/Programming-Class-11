fruit={}
L1=["Apple","banana","apple"]
for index in L1:
    if index in fruit:
        fruit[index]+=1
    else:
        fruit[index]=1
print(len(fruit))
print(fruit)
