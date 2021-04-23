p=int(input("Enter Principal :"))
r=int(input("Enter Rate of Interest :"))
t=int(input("Enter Duration (in Years) :"))
si=(p*r*t)/100
A = p * (pow((1 + r / 100), t))
ci = A - p
print("Simple Interest :",si)
print("Compound Interest :",ci)
