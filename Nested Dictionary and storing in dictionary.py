d={}
n=int(input('Enter number of the Student :'))
for i in range(n):
  a=input('Enter name of the winner:')
  b=int(input('Enter the number of wins of the Student:'))
  d[a]=b
print('\n')
print('Name of the Student','\t','Number of Wins')
for i in d:
   print('\t','\t',i,'\t','\t','\t','\t','\t','\t',d[i])
print("\n")
print("\n")
print("\n")


people = {1: {'Name': 'Aniket', 'Class': '11', 'Sec': 'A'}, 2: {'Name': 'Biswas', 'Age': '16', 'gender': 'male'}}
print(people)
print(people[1])
print(people[2])
