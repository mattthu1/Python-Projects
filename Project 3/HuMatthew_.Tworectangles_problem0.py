#gathering input from user about lengths and widths of the two triangles

width1 = int(input("Enter the width for Rectagnle #1: "))
length1 =int(input("Enter the length for Rectagnle #1: "))
width2 = int(input("Enter the width for Rectagnle #2: "))
length2 =int(input("Enter the length for Rectagnle #2: "))

#creating the area and storing them in variables

Rectangle1 = width1 * length1 
Rectangle2 = width2 * length2

#printing the areas of the two triangles

print("#1 has an area of", Rectangle1)
print("#2 has an area of", Rectangle2)

if width1 == length1:
      print('Rectangle 1 is a square')

if width2 == length2:
      print('Rectangle 2 is a square')

#printing the if else statements to say which rectangle is larger

if Rectangle1 > Rectangle2:
    print("Rectangle 1 is larger than Rectangle 2")

elif Rectangle1 < Rectangle2:
    print("Rectangle 2 is larger than Rectangle 1")

else: 
     print('TRectangle #1 and Rectangle #2 are the same size!')




