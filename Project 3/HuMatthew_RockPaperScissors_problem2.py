import random

#importing random

print('Rock, Paper, Scissors')

answer = input("Rock, paper, or scissors? ")

if answer == 'rock' or answer == 'Rock':
     human = 'Rock1'

elif answer == 'paper' or answer == 'Paper':
     human = 'Paper1'

elif answer == 'scissors' or answer == 'Scissors':
     human = 'Scissors1'

else: 
    print('That is not a valid option. Please try again!')
    exit()
    
#gathering the information from the users and stroring them in their respected variables 

cpu = random.randint(1,3) 

#storing the random integer from the computer into a variable

if cpu == 1:
     print('The computer played Rock.')
     cpuoutput = 'Rock2'

elif  cpu == 2:
     print('The computer played Paper.')
     cpuoutput = 'Paper2'

elif cpu == 3:
     print('The computer played Scissors.')
     cpuoutput = 'Scissors2'

#creating an if else statement and storing the integers into variables 

if (cpuoutput == 'Rock2' and human == 'Scissors1' ):

 print('You Lose!')

elif (cpuoutput == 'Scissors2' and human == 'Paper1' ):
 print('You Lose!')

elif (cpuoutput == 'Paper2' and human == 'Rock1'):
     print('You Lose!')

#creating an if else statement for if the user loses


if (cpuoutput == 'Rock2' and human == 'Rock1') :
    print('You tie!')
    
elif (cpuoutput == 'Scissors2' and human == 'Scissors1' ):
    print('You tie!')

elif (cpuoutput == 'Paper2' and human == 'Paper1'):
    print('You tie!')
     
#creating an if else statement for if the user ties


if (cpuoutput == 'Rock2' and human == 'Paper1'):
    print('You Win!')
elif(cpuoutput == 'Scissors2' and human == 'Rock1' ) :
    print('You Win!')
elif (cpuoutput == 'Paper2' and human == 'Scissors1'):
     print('You Win!')

#creating an if else statement for if the user wins



