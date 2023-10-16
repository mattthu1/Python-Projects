
import random

#importing 'random' package

balance = float(input("To begin, enter how much money you would like to initially borrow (i.e. 2000):  "))
lower_bound = float(input("Next, enter a lower bound for the monthly interest rate. For example, enter 5 for 5%: "))
upper_bound = float(input("EFinally, enter a lower bound for the monthly interest rate. For example, enter 10 for 10%: "))

#asking the user for the initlal loan amount and their lower/upper bound

print("------- Calculating --------")
print("Month     Starting Balance    Interest Rate    Ending Balance")

interest_rate1 = random.randint(lower_bound,upper_bound)
interest_rate2 = random.randint(lower_bound,upper_bound)
interest_rate3 = random.randint(lower_bound,upper_bound)

#creating the random interest rate value 

ending_balance1 =((interest_rate1/100)+1)* balance
ending_balance2 =((interest_rate2/100)+1)* ending_balance1
ending_balance3 =((interest_rate3/100 )+1)* ending_balance2

#multiplying the random interest value to the previous balance in order to get the ending balance

balance_format = '$' + format(balance,',.2f')

interest_rate1_format = format(interest_rate1) + '%'
interest_rate2_format = format(interest_rate2) + '%'
interest_rate3_format = format(interest_rate3) + '%'

ending_balance_format1 = '$' +format(ending_balance1, ',.2f')
ending_balance_format2 = '$' +format(ending_balance2, ',.2f')
ending_balance_format3 = '$' +format(ending_balance3, ',.2f')

#formatting the variables so that it will ad "$", "%" , commas and periods. 

print(1, '        ' , balance_format, '           ' ,   interest_rate1_format,  '         ' ,     ending_balance_format1   )
print(2, '        ' , ending_balance_format1, '           ' ,   interest_rate2_format,  '         ' ,     ending_balance_format2   )
print(3, '        ' , ending_balance_format2, '           ' ,   interest_rate3_format,  '          ' ,     ending_balance_format3   )


#printing out the final result