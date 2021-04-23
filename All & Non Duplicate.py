a=int(input("Enter a="))
b=int(input("Enter b="))
c=int(input("Enter c="))
sum1=(a+b+c)
print("Sum of",a,"+",b,"+",c ,"is",sum1)
if a==b:
    sum1=(b+c)
    print("Non Duplicate Sum=",sum1)
elif a==c:
    sum2=(a+b)
    print("Non Duplicate Sum=", sum2)
elif b==c:
    sum3=a+c
    print("Non Duplicate Sum=", sum3)


