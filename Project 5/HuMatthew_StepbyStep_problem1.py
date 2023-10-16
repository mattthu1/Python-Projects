number = int(input('Pick a number to go up to:'))

while number < 0:
    print('Invalid, try again.')
    
    number = int(input('Pick a number to go up to:'))



for i in range(1, number+1):
    for j in range(1, i+1):
        print(j, end=" ")

    print()
        
        