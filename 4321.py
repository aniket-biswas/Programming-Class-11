n=int(input("Enter the no of columns required: "))
row =1
while (row<=n):
   col=n
   while (col>= row):
     print (col, end=" ")
     col = col-1
   row=row+1
   print ()
