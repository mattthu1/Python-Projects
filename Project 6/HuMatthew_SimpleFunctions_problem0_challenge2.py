#Function: valid_date

#Input: Two integer arguments - a month (month), and a day (day)


#Processing: if month is not between 1 and 12, it  return False
#if day is not between 1 and 31, it returns return False
#if month is 2 and day is greater than 28, it return False
#if month is in April, June, September, November and the day is greater than 30, it returns False
#Otherwise, return True


#Output: A boolean value (True if the date is valid, False if the date is invalid)



#defining cariables
def valid_date(month, day):

    #creating statments for what is false

    if month < 1 or month > 12:
        return False
    if day < 1 or day > 31:
        return False
    if month == 2 and day > 28:
        return False
    if month in [4, 6, 9, 11] and day > 30:
        return False
    return True

# Test 
print(valid_date(99,1)) # False
print(valid_date(1,99)) # False
print(valid_date(99,99)) # False
print(valid_date(-99,1)) # False
print(valid_date(1,-99)) # False
print(valid_date(-99,-99)) # False
print(valid_date(9,25)) # True
print(valid_date(10,15)) # True
print(valid_date(11,31)) # False
print(valid_date(2,28)) # True
print(valid_date(2,29)) # False
