#ask the user what he rolled on his first dice
valid1 = False
while valid1 == False:
 dice1 = int(input("What was your first roll?"))
 if dice1 >= 1 and dice1 <= 6:
  valid1 = True
 else:
  print("Invalid, try again!")
#ask the user what he rolled on his second dice
valid2 = False
while valid2 == False:
 dice2 = int(input("What was your second roll?"))
 if dice2 >= 1 and dice2 <= 6:
  valid2 = True
 else:
  print("Invalid, try again!")
#two even rolls
if dice1%2 == 0 and dice2%2 == 0:
 print("Evens!")
#two odd rolls
if dice1%2 == 1 and dice2%2 == 1:
 print("Odds!")
#sum roll
if dice1 + dice2 == 6:
 print("Sum!")
#high/low
if dice1 == 1 and dice2 == 6 or dice1 == 6 and dice2 == 1:
 print("High/Low roll!")
#snake eyes
if dice1 == 1 and dice2 == 1:
 print("Snake Eyes!")