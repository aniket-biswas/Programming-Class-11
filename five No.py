a=float(input("Enter 1st no="))
b=float(input("Enter 2nd no="))
c=float(input("Enter 3rd no="))
d=float(input("Enter 4rd no="))
e=float(input("Enter 5th no="))
choice=float(input("Choose any no out of the five no entered="))
if choice==a:
    sum1=a*1,a*2,a*3
    print("Multiple of",a,"are",sum1,"...")
elif choice==b:
    sum2=b*1,b*2,b*3
    print("Multiple of",b,"are", sum2,"...")
elif choice == c:
    sum3 = c * 1, c * 2, c * 3
    print("Multiple of",c,"are", sum3,"...")
elif choice==d:
    sum4=d*1,d*2,d*3
    print("Multiple of",d,"are", sum4,"...")
elif choice==e:
    sum5=e*1,e*2,e*3
    print("Multiple of",e,"are", sum5,"...")
else:
    print("!Invalid Choice!")


