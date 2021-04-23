#WAP to find the multiples of a number (the divisor) out of five numbers.
div=float(input("Enter no="))
b=float(input("Enter Multiple no 1="))
c=float(input("Enter Multiple no 2="))
d=float(input("Enter Multiple no 3="))
e=float(input("Enter Multiple no 4="))
f=float(input("Enter Multiple no 5="))
if b%div==0:
    print("B is a multiple of A")
elif c%div==0:
    print("C is a multiple of A")
elif d%div==0:
    print("D is a multiple of A")
elif e%div==0:
    print("E is a multiple of A")
elif f%div==0:
    print("F is a multiple of A")
else:
    print("Not multiple")
