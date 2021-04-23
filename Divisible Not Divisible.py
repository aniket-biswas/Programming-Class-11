a=float(input("Enter 1st no="))
b=float(input("Enter 2nd no="))
mod = a % b
quo=a/b
print("Quotient", quo)
print("Remainder", mod)
if mod==0:
    print(a," is Divisible by ",b)
else:
    print("Not Divisible by another no")

