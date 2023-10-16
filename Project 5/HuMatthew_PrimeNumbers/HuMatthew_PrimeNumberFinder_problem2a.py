number = int(input('Enter a positive number to test:'))
print()

prime = False

while number <= 0:
      print('Invalid. Please try again')
      number = int(input('Enter a positive number to test:'))
      print()




if number% 2==  0:
        print (f'2 is a divisor of {number} ... stopping')
        print()
        if number == 2:
               print(f'{number} is  a prime number!')

        else:
               print(f'{number} is not a prime number!')
        exit()
        

else:
        print(f'2 is NOT a divisor of {number} ... continuing')
        prime = True


if number% 3==  0:
        print (f'3 is a divisor of {number} ... stopping')
        print()
        if number == 3:
               print(f'{number} is  a prime number!')

        else:
               print(f'{number} is not a prime number!')
        exit()
        
else:
     print(f'3 is NOT a divisor of {number} ... continuing')
     prime = True
    


if number% 4 ==  0:
        print (f'4 is a divisor of {number} ... stopping', )
        print()
        print(f'{number} is not a prime number!')
        exit()

else:
        print(f'4 is NOT a divisor of {number} ... continuing' )
        print()
        prime = True


    
if number == 1 :
    print(f'{number} is technically not a prime number!')
    


elif prime == True:
    print(f'{number} is a prime number!')



