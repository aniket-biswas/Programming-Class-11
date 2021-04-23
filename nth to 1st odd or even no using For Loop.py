print("!Important Message!")
print("# If you want odd no please input 1st no as Odd #")
print("# If you want even no please input 1st no as even #")
a=int(input("Enter Starting No(According to You Ending No)="))
b=int(input("Enter Ending No(Accoridng to you Starting No)="))
if a == b:
  print("!Invalid! **Both the values are Same**")
for i in range(b,a,-2):
  print(i)
