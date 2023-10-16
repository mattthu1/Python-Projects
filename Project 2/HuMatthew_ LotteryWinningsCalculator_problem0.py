total = int(input('How much money did you win?'))
people = int(input('How many people are splitting the winnings?'))
tax = int(input('What is the tax rate on winnings? (i.e. 25 = 25%):'))

#receive input from user about input money won, people who are splitting and the tax rate

money_per_person = total/people
tax_per_person = money_per_person *tax/100
take_home_per_person = total/people*(1-(tax/100))

#divide the tax rate by how many people are diving and figuring out the take home per person

total_format = '$' + format(total,',.2f')
money_per_person_format = '$'+format(money_per_person, ',.2f')
tax_per_person_format = '$' +format(tax_per_person, ',.2f')
take_home_per_person_format = '$' +format(take_home_per_person, ',.2f')

#formatting the variables so that they have commas, periods and dollar signs in their corresponding location 

print('In total you won',total_format)
print("Split 4 ways that amounts to", money_per_person_format , "per person")
print('Tax per person: ', tax_per_person_format)
print('Take home amount per person:  ', take_home_per_person_format)