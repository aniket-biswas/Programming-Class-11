n1=str(input("Enter Employee name:"))
d=str(input("Enter Designation:"))
b=int(input("Enter Basic Salary:"))
da=b*0.25
hra=b*0.20
pf=b*0.125
n=b+da-hra-pf
print("Employee Name:",n1)
print("Designation:",d)
print("DA:Rs.",da,"HRA:Rs.",hra,"PF:Rs.",pf)
print("Net Salary:Rs.",n)

