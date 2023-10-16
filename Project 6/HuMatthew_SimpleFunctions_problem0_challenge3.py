#Function: simple_sort

#Input: Three integer arguments are taken in 

#Processing: The function sorts the integers in ascending order 

#Output: A tuple of the sorted integers



def simple_sort(num1, num2, num3):
    smallest = min(num1, num2, num3)
    largest = max(num1, num2, num3)
    middle = (num1 + num2 + num3) - smallest - largest
    return (smallest, middle, largest)


#test

a,b,c = simple_sort(10,20,30)
print(a,b,c) # 10 20 30
a,b,c = simple_sort(10,30,20)
print(a,b,c) # 10 20 30
a,b,c = simple_sort(30,20,10)
print(a,b,c) # 10 20 30
a,b,c = simple_sort(30,20,20)
print(a,b,c) # 20 20 30