a=float(input("Enter 1st no="))
b=float(input("Enter 2nd no="))
c=float(input("Enter 3rd no="))
if a>b>c:
    print("Descending Order=",a,"{1st no}",b,"{2nd no}",c,"{3rd no}")
elif a>c>b:
    print("Descending Order=",a,"{1st no}",c,"{3rd no}",b,"{2nd no}")
elif b>a>c:
    print("Descending Order=",b,"{2nd no}",a,"{1st no}",c,"{3rd no}")
elif b>c>a:
    print("Descending Order=",b,"{2nd no}",c,"{3rd no}",a,"{1st no}")
elif c>a>b:
    print("Descending Order=",c,"{3rd no}",a,"{1st no}",b,"{2nd no}")
elif c>b>a:
    print("Descending Order=",c,"{3rd no}",b,"{2nd no}",a,"{1st no}")

