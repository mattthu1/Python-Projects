contact_num = int(input('How many contacts would you like to add?'))

#if the email is invalid, it will say so

while contact_num < 0:

    print('Invalid, please try again')
    contact_num = int(input('How many contacts would you like to add?'))

#determining whether if the name is valid

contacts_dict = {}
for i in range(1, contact_num+1):
    contacts = input(f'Please enter the name of contact {i}: ')
    
    while (contacts.isdigit()) or not (' ' in contacts):
        print('Invalid, please try again')
        contacts = input(f'Please enter the name of contact {i}: ')

    email = input(f'Please enter the email of contact {i}: ')

    #gathering all the information which determines a correct domain

    domain = False
    for x in range(len(email)):
        if email[x] == '@':
            start = x + 1
    for j in range(start, len(email)-4):
        if not email[j].isalpha() and not email[j].isdigit():
            domain = False
            break
    else:
        domain = True

    #gathering all the information which determines a correct email


    while not email.endswith('.com'):
        print('Invalid, please try again')
        email = input(f'Please enter the email of contact {i}: ')

#creating all the aspects of the email
    while not ('@' in email) or not email[0].isalpha() or not domain:
        print('Invalid, please try again')
        email = input(f'Please enter the email of contact {i}: ')

    contacts_dict[contacts] = email


#giving the address book

print('Thanks! Here is your address book:')

for contact, email in contacts_dict.items():
    print(f'Name: {contact}, Email: {email}')
