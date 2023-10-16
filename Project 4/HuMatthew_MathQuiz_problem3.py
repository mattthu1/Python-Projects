#importing random
import random

#setting the variables to 0
counter = 0
correct = 0 


#creating a loop that ends once the conditions are met
while True:
   
    #randomly generating the first and second number 
    Q1_1 = random.randint(1, 10)
    Q1_2 = random.randint(1, 10)

    #generating a random number in order to randomly get addition, subtraction or multiplication
    operator = random.randint(1, 3)
    
    if operator == 1: 
        operator1 = '+'
    elif operator == 2:
        operator1 = '-'
    else:
        operator1 = '*'

    if operator1 == '+':
        answer1 = Q1_1 + Q1_2
    elif operator1 == '-':
        answer1 = Q1_1 - Q1_2
    else:
        answer1 = Q1_1 * Q1_2

#printing what the numbers along with the operators to create a math problem 

    print(f'Question {counter + 1}. {Q1_1} {operator1} {Q1_2}') 
    answer = int(input('What is the answer? '))
   
   #if the answer is correct, it will display that it is correct then it will be correct and add 1 to each the number of times it has iterated and the correct counter
    if answer1 == answer:
        print('Correct!')
        counter += 1
        correct += 1
   
   # if the answer is incorrect, it adds to the counter and displays incorrect 
    elif answer1 !=answer:
        print('Incorrect!')
        counter += 1

    
    #the score/grade will then appear pout of five and give the user back a letter grade. 
    if counter == 5:
        print(f'You received {correct} out of a possible 5 points.')

        if correct < 2:
            print('You scored an F')
        elif correct == 2:
         print('You scored a D')
        elif correct == 3:
         print('You scored a C')
        elif correct == 4:
         print('You scored a B')
        else:
            print('You scored an A')

        
        break