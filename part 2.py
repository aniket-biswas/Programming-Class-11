a=int(input("Enter a="))
b=int(input("Enter b="))
c=int(input("Enter c="))
if a==b:
    sum1=(b+c)
    print("non Duplicate Sum=",sum1)
elif a==c:
    sum2=(a+b)
    print("non Duplicate Sum=", sum2)
elif b==c:
    sum3=a+c
    print("Non Duplicate Sum=", sum3)
