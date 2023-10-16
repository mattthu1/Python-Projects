date = int(input('Enter a date in YYYYMMDD format (i.e. 20230219 for February 19th, 2023:'))

#collecting the date from the user

startschool = 20230123
endschool = 20230123

#starting the start and end of the semester

year = date // 10000
month = (date // 100) % 100
day = date % 100

#establishing years, months and days

month = (date // 100) % 100
month0 = int('{:02d}'.format(month))


day = (date // 1) % 1000
day0 = int('{:02d}'.format(day))

#formatting the months and days and isolating them into months/days

if 131 < day0 < 200 or 228< day0 < 300 or 331 < day0 < 400 or 430 < day0 < 500 or 531< day0 < 600 or 630 < day0 < 700 or 731< day0 < 800 or 831< day0 < 900 or 931<  day0 < 1000 or 1032< day0 < 1100 or 1130 <  day0 < 1200 or 1231< day0 <1300 : 
    print('This date is invalid')
    exit()
    
    #making it so that if the date is above the amount of days the month has, it is invalid

elif date < 20230123:
    print('This date is before the semester begins')

    #if the user enters the date before the semster started, it will say so

elif date > 20230508:
    print('This date is after the semester ends')

     #if the user enters the date after the semster started, it will say so


elif (day % 7 == 1) or (day % 7 == 2):
        print('You don’t have class today')
   
    #if the user enters a weekend, it will tell the user that they don't have class that day

else: 
     print('You have class today')

     #if none of the above statements apply, then the user has school


