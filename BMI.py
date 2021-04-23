kg=float(input("Enter Weight in Kilogram:"))
h=float(input("Enter height in Metres:"))
b=kg/(h*h)
if ( b < 18):
   print("BMI:",b,"kg/m^2 Status:Underweight")
elif ( b >= 18.5 and b < 24.9):
   print("BMI:",b,"kg/m^2 Status:Normal")
elif ( b >= 25 and b < 29.9):
   print("BMI:",b,"kg/m^2 Status:Overweight")
elif ( b >=30):
   print("BMI:",b,"kg/m^2 Status:Obese")


