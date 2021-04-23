l = []
n = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, n + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    l.append(value)
l.sort()
print("The Second Largest Element in this List is :", l[n - 2])

