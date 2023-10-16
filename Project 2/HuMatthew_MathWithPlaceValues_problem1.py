
value1 = int(input("Enter a number between 0 and 999: "))
value2 = int(input('Enter another number between 0 and 999: '))

#asking user for two numbers between 0-999

ones = (value1 % 10) + (value2 % 10)
tens = ((value1 // 10) % 10) * ((value2 // 10) % 10)
hundreds = (value1 // 100) - (value2 // 100)

#finding each of the differences between values given

print("Sum of ones =", (value1 % 10), "+", (value2 % 10), "=", ones)
print("Product of tens =", ((value1 // 10) % 10), "*", ((value2 // 10) % 10), "=", tens)
print("Difference of hundreds = ", (value1 // 100), "-", (value2 // 100), "=", hundreds)