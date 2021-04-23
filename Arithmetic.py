a=float(input("Enter a="))
b=float(input("Enter b="))
oper=input("Choose a math operation (+,/,%,**, -, *): ")
if oper=='+':
    s1=a+b
    print(a,"Added to",b,"gives",s1)
elif oper=='/':
    s2=a/b
    print(a,"Divided By",b,"gives quotient",s2)
elif oper=='%':
    s3=a%b
    s7=a/b
    print(a,"When Divided by",b,"gives remainder",s3, "& quotient=",s7)
elif oper=='**':
    s4=a**b
    print(a,"to the power",b,"gives",s4)
elif oper=='-':
    s5=a-b
    print(a,"subtracted from",b,"gives",s5)
elif oper=='*':
    s6=a*b
    print(a,"multiplied by",b,"gives",s6)
else:
    print("!Entered Invalid Arithmetic Operator!")