d={}
n=int(input("Enter No of Students:"))
for i in range (n):
  a=input('Enter name of the Student:')
  b=int(input('Enter the Roll no of the Student:'))
  c=int(input("Enter Age of the student:"))
  e=input("Enter Field:")
  d[a]=b
print('\n')
print('Name of the Student','\t','Roll No',"\t","Age","\t","Field")
for i in d:
   print('\t','\t',i,'\t','\t',"\t",'\t','\t',d[i],'\t',c,'\t',e)
