x=float(input("Enter the Base:"))
n=int(input("Enter the Exponent:"))
s=0
for a in range(n+1):
    s=s+x**a
    print("Sum of Series=",s)
