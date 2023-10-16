# Ask the username and create variables
name = input('Enter a username: ')
b = False

# Define a function to count the number of uppercase, lowercase, and digit characters
def count_chars(name):
    uppers = 0
    lowers = 0
    digits = 0
    for c in name:
        if c.isupper():
            uppers += 1
        elif c.islower():
            lowers += 1
        elif c.isdigit():
            digits += 1
    return uppers, lowers, digits

# Define a function to validate the username
def validate_username(username):
    # Check username length
    if len(username) < 8 or len(username) > 15:
        print('Username is invalid, please try again')
        return False
    
    # Check for valid characters
    if not username.isalnum():
        print('Username is invalid, please try again')
        return False
    
    # Check first and last characters
    if username[0].isdigit() or username[-1].isdigit():
        print('Username is invalid, please try again')
        return False
    
    # Check for at least one uppercase, one lowercase, and one numeric character
    uppers, lowers, digits = count_chars(username)
    
    if uppers == 0 or lowers == 0 or digits == 0:
        print('Username is invalid, please try again')
        return False
        
    # If all checks pass, username is valid
    print('Username is valid!')
    return True

# Loop until a valid username is entered
while not b:
    # Print username information
    uppers, lowers, digits = count_chars(name)
    print(f'* Length of username: {len(name)}')
    print(f'* All characters are alpha-numeric: {name.isalnum()}')
    print(f'* First and last characters are not digits: {not (name[0].isdigit() or name[-1].isdigit())}')
    print(f'* # of uppercase characters in the username: {uppers}')
    print(f'* # of lowercase characters in the username: {lowers}')
    print(f'* # of digits in the username: {digits}')
    
    # Validate the username
    b = validate_username(name)
    
    # If the username is invalid, ask for a new one
    if not b:
        name = input('Enter a username: ')
