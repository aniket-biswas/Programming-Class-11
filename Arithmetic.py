a=float(input("Enter a="))
b=float(input("Enter b="))
oper=input("Choose a math operation (+,/,%,**, -, *): ") # Choice of operator
if oper=='+':
    s1=a+b # Addition 
    print(a,"Added with",b,"gives = ",s1)
elif oper=='/':
    s2=a/b # Quotient
    print(a,"Divided By",b,"gives quotient = ",s2)
elif oper=='%':
    s3=a%b  # Remainder
    s7=a/b
    print(a,"When Divided by",b,"gives remainder",s3, "& quotient=",s7)
elif oper=='**':
    s4=a**b # Power (Exponent)
    print(a,"to the power",b,"gives = ",s4)
elif oper=='-':
    s5=a-b # Subtraction
    print(a,"subtracted from",b,"gives = ",s5)
elif oper=='*':
    s6=a*b # Multiplication
    print(a,"multiplied by",b,"gives = ",s6)
else:
    print("!Entered Invalid Arithmetic Operator!")
