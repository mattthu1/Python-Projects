day = 1
days_sales = {}


#asking for sales

while day < 8:
    sales = int(input(f'Sales for day {day}: '))

    while sales < 0:
        print('Sorry, that is not a valid amount. Please try again.')
        sales = int(input(f'Sales for day {day}: '))

    days_sales[day] = sales
    day += 1


#creating the sums of all the sale and getting the averages, max and mins

sum = int(days_sales[1] +days_sales[2]+ days_sales[3] + days_sales[4] + days_sales[5]+ days_sales[6] + days_sales[7] )
average = sum/7
max_sales = max(days_sales, key=days_sales.get)
min_sales = min(days_sales, key=days_sales.get)



print(f'Total sales: {sum}')
print(f'Average sales per day: {average}')
print(f'Highest sales day: {max_sales}')
print(f'Lowest sales day: {min_sales}')

