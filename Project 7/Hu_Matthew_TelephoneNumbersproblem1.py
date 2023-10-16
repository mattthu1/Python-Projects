#ask user for input
number = int(input('What is your phone number?'))

#if number is less than 10 digits, then tell user so
while len(str(number)) < 10:
    print('Phone number is too short, please try again!')
    number = int(input('What is your phone number?'))


 #if number is more than 10 digits , then tell user so
while len(str(number)) > 10:
    print('Phone number is too long, please try again!')
    number = int(input('What is your phone number?'))


#if the length is correct, then tell the user thier number
print(f'Your phone number is +1 ({str(number)[0:3]}) {str(number)[3:6]}-{str(number)[6:]}')

