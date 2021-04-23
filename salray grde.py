a=input("Enter Grade:")
s=int(input("Enter Salary:"))
a=a.lower()
if a=='a':
  d=s*0.3
  print(d)
elif a=="b":
  d=s*0.25
  print(d)
elif a=="c":
  d=s*0.20
  print(d)
else:
  d=s*0.05
  print(d)