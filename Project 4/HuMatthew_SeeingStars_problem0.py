#getting the first number from the user
number1 = int(input("Number 1: "))


#creating a loop where if the user inputs a negative number then it will ask again
while number1 < 0: 
   print(" Invalid, try again")
   number1 = int(input("Number 1: "))
    

else:
   num1 = ("*" * number1)


number2 = int(input("Number 2: "))
   
#creating a loop where if the user inputs a negative number or a number less than the first number it will ask again

while number2 < 0 or number1 >= number2: 
   print(" Invalid, try again")
   number2 = int(input("Number 2: "))




else:
   num2 = ("*" * number2)

#using a fo r loop to print the ascneding amount of "*" 

for i in range(len(num1), len(num2) + 1):
    nums = '*' * i
    print(nums)

#using a fo r loop to print the descending amount of "*" 


for i in range(len(num2) - 1, len(num1) - 1, -1):
        nums = '*' * i
        print(nums)