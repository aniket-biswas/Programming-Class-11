import cmath
print('#a should not be equal to zero#')
a=float(input("Enter a="))
b=float(input("Enter b="))
c=float(input("Enter c="))
Discriminant=(b**2)-(4*a*c)
Alpha=(-b+cmath.sqrt(Discriminant))/(2*a)
Beta=(-b-cmath.sqrt(Discriminant))/(2*a)
print("Root 1=",Alpha)
print("Root 2=",Beta)



