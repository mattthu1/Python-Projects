#set valid to False and use to control while loop
valid = False
while valid == False:
 num = int(input("Tell me your number:" ))
#needs a positive number to proceed
 if num >= 0:
    valid = True
#otherwise, ask for another number
 else:
    print("Invalid, try again!")
#even numbers
if num%2 == 0:
 print("Your number is even!")
#divisible by 4
 if num%4 == 0:
    print("Cool!")
#divisible by 5
 if num%5 == 0:
    print("Wow!")
#odd numbers
else:
 print("Your number is odd!")
#divisible by 5
 if num%5 == 0:
    print("Great!")