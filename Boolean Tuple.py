t=(1,2,3,4,5,6)
n=int(input("Enter NO:"))
B=False
for i in range(len(t)):
    if t[i]==n:
        B=True
if B==True:
    print("Found")
else:
    print("Not Found")


