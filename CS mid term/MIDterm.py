sum = 0
sum1 = 0


for i in range(1,21):

    
    integer = int(input('Enter an integer:'))    
    
    while integer < 0: 
    
        print('Invalid, integer regected')

        integer = int(input('Enter an integer:'))
        print()

    while not (integer%3 ==0 and integer%6 == 0):
            
            print('Invalid, integer rejected')
        
            integer = int(input('Enter an integer:')) 
            
    else:
        
            print('Valid integer!')
            sum+= integer
       

       
        
            

    
        
        

print(f'Successfully collected {i} integers, stopping')
print(f'Total is:{sum}')