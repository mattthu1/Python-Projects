#importing the randoms

import random
import digitalclock
correct = 0
count = 0


#asking the user for the inpuit

num_problems = int(input("How many problems would you like to attempt?"))
while num_problems <= 0:
    print("Invalid number, try again")
    num_problems = int(input())


width = int(input("How wide do you want your digits to be? 5-10:"))
while width < 5 or width > 10:
    width = int(input("Invalid width, try again"))

character = input("What character would you like to use?")
while len(character ) != 1:
    character = input("String too long, try again")

print("Here we go!")

print("What is ..... ")


#creating loop to go as many times as user wants

while count < num_problems:


    #printing the numbers

    number1 = random.randint(0, 9)
    number2 = random.randint(0, 9)
    operator = random.choice(['+', '-'])

    if operator == '+':
        answer = number1 + number2
        temp = digitalclock.plus(width, character)
    else:
        answer = number1 - number2
        temp = digitalclock.minus(width, character)
        
        

    digitalclock.print_number(number1, width, character)
    print(temp)
    digitalclock.print_number(number2, width, character)
    print("=")

    user_answer = int(input())


    #stating whether it is correct or not 


    if user_answer == answer:
        print("Correct!")
        correct += 1
    else:
        print("Sorry, that's not correct.")
    
    count += 1

#saying how many they got wrong

print("You got", correct, "out of", num_problems, "correct!")
