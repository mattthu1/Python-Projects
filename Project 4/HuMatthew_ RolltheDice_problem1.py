#importing random
import random

#creating the variables and settingt them to 0
rolecount = 0 
doubles = 0
highvalue = 0  
evens = 0 
odds = 0 
highlow = 0 
sumvalue = 0 


#asking the user how many sides they want for the dice
sides = int(input('How many sides on your dice(4, 6, 8)? '))


#creating a loop for that if it gets anything other than 4, 6, or 8 it will ask the user again
while sides not in [4, 6, 8]:
    print('Invalid size, try again.')
    sides = int(input('How many sides on your dice? '))

else:
    print('Thanks, here we go!')

#creating loop that repeats until the user gets snake eyes (1 and 1)
while True:
    die1 = random.randint(1, sides)
    die2 = random.randint(1, sides)
    rolecount += 1

    value = True 

    if die1 == 1 and die2 == 1:
        print(f'die #1 is *{die1}* and die #2 is *{die2}* Odds! Doubles! Snake Eyes!')
        
        
        doubles += 1 
        odds += 1


        print(f'You finally got snake eyes on roll #{rolecount}')
        break


       
#creating the condition where if it is even, then it will say so, and if it is doubles, it will say so and also say even
#evens double
    if (((die1 == die2 )) and (die2 == 2 or die2 == 4 or die2 == 6 or die2 == 8)) and (die2 == 2 or die2 == 4 or die2 == 6 or die2 == 8):

        print(f'die #1 is *{die1}* and die #2 is *{die2}* Evens! Doubles!')

        rolecount = rolecount + 1
        doubles += 1
        value = False


#evens
    elif ((die1 == 2 or die1 == 4) or (die1 == 6 or die1 == 8)) and (die2 == 2 or die2 == 4 or die2 == 6 or die2 == 8):
        print(f'die #1 is *{die1}* and die #2 is *{die2}* Evens!')
        
        evens += 1
        rolecount += 1
        value = False
        


#creating the condition where if it is odd, then it will say so, and if it is doubles, it will say so and also say odd
#odds double
    if (die1 == die2) and (die2 == 1 or die2 == 3 or die2 == 5 or die2 == 7)and (die2 == 1 or die2 == 3 or die2 == 5 or die2 == 7):

        print(f'die #1 is *{die1}* and die #2 is *{die2}* Odds! Doubles!')

        rolecount = rolecount + 1
        doubles += 1
        value = False



#odds
    elif (die1 == 1 or die1 == 3 or die1 == 5 or die1 == 7) and (die2 == 1 or die2 == 3 or die2 == 5 or die2 == 7):
            print(f'die #1 is *{die1}* and die #2 is *{die2}* Odds!')
            
            odds += 1
            rolecount = rolecount + 1
            value = False

    



#if the user rolls the highest number and the lowest number it will say so
#high/low
    elif (die1 == sides and die2 == 1) or (die1 == 1 and die2 == sides):
        print(f'die #1 is *{die1}* and die #2 is *{die2}* High/ Low!')
       
        rolecount = rolecount + 1
        highlow += 1
        value = False



#creating the condition where if it is even, or odd as well as the two values add up to the number of sides on the die, it will say so. adiditonally if it rolls 3 and 3 it will say all that it needs to
#size value odds
    if (die1 + die2 == sides) and (die1 == 1 or die1 == 3 or die1 == 5 or die1 == 7) and (die2 == 1 or die2 == 3 or die2 == 5 or die2 == 7):
        print(f'die #1 is *{die1}* and die #2 is *{die2}* Odds! Sum value is size value!')
        
        rolecount = rolecount + 1
        odds += 1
        sumvalue +=1
        value = False


    elif (die1 + die2 == sides) and (die1 == 2 or die1 == 4 or die1 == 6 or die1 == 8) and (die2 == 2 or die2 == 4 or die2 == 6 or die2 == 8):
        print(f'die #1 is *{die1}* and die #2 is *{die2}* Evens! Sum value is size value!')
        
        rolecount = rolecount + 1
        evens += 1
        sumvalue +=1
        value = False
        
        
    elif die1 + die2 == sides:
        print(f'die #1 is *{die1}* and die #2 is *{die2}* Sum value is size value!')
    
        
        rolecount += 1
        sumvalue +=1
        value = False


    elif die1 == 3 and die2 == 3:
        print(f'die #1 is *{die1}* and die #2 is *{die2}* Odds! Doubles! Sum value is size value!')

        rolecount = rolecount + 1
        doubles += 1
        sumvalue +=1
        value = False
        

    #if it rolls two values that are both equal and the side of the die, it will tell you it rolled two high values
   #2highvalues
    if die1 == sides and die2 == sides:
        print(f'die #1 is *{die1}* and die #2 is *{die2}* High Roll')
        
        rolecount += 1
        highvalue +=1
        value = False
    
    if value == True:
        print(f'die #1 is *{die1}* and die #2 is *{die2}*')
        rolecount += 1
   

    

#formatting the variables so they can be presented in a percentage form        
doublesp = doubles /rolecount       
highvaluep = highvalue/rolecount
evensp = evens/rolecount
oddsp = odds/rolecount 
highlowp = highlow/rolecount
sumvaluep = sumvalue/rolecount 

doubles_format = format(doublesp * 100 ,',.2f')+ '%'
highvaluep_format = format(highvaluep * 100, ',.2f')+ '%'
evensp_format = format(evensp * 100, ',.2f')+ '%'
oddsp_format = format(oddsp * 100, '.2f')+ '%'
highlowp_format = format(highlowp * 100, '.2f')+ '%'
sumvaluep_format = format(sumvaluep * 100, '.2f') + '%'



#displaying the information so to give the information about how many times _____ was rolled 
print('Along the way you rolled DOUBLES', doubles,'times. (' ,doubles_format ,  'of all rolls were doubles)')


print('Along the way you rolled TWO HIGH VALUES',highvalue,'times (' , highvaluep_format  ,   ' of all rolls were twohigh values)')


print('Along the way you rolled EVENS', evens,'times. (', evensp_format ,  'of all rolls were evens)')


print('Along the way you rolled ODDS', odds,'times. (' ,oddsp_format ,  'of all rolls were odds)')


print('Along the way you rolled HIGH / LOW ', highlow,'times. (', highlowp_format,    'of all rolls were high/low)')

                                            
print('Along the way you rolled SUM VALUE ', sumvalue,'times. ('  , sumvaluep_format ,   'of all rolls were sumvalue )')

