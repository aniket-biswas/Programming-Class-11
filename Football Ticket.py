age=int(input("Enter Age="))
if (age >= 11):
  print ("You are eligible to see the Football match.")
  if (age <= 20 or age >= 60):
      print("Ticket price is $12")
  else:
      print("Ticket price is $20")
else:
    print ("You're not eligible to buy a ticket.")