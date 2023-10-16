print('Triangle Tester')

#gathering the information about the sides of the traingles 

a = int(input("What is the length of side 1? "))
b = int(input("What is the length of side 2? "))
c = int(input("What is the length of side 3? "))

if a + b > c and  b + c > a and a + c > b:
    print("This is a valid triangle!")

    #creating the criteria for makes it a triangle

    print("The perimeter of the triangle is ", a + b + c)
    
    if a == b == c:
         print('This is an equilateral triangle ') 

         #declaring what makes a equalateral triangle

    elif a == b or b == c or c == a: 

          #declaring what makes an isosceles triangle 

        print('This is an isosceles triangle ') 
        
        # checking if the triangle is also a right-angled triangle
        if a*a + b*b == c*c or a*a + c*c == b*b or c*c + b*b == a*a:
            print('This is also a right-angled triangle')
    
    else:
         print('This is an scalene triangle ') 

         #declaring what makes an scalene triangle         
          
         if (a*a + b*b == c*c) or (a*a + c*c == b*b) or (c*c + b*b == a*a):
              print('This is also a right triangle')
        
         #stating whether the triangle is a right triangle or not
    
else:
     print("This is not a valid triangle!")

#declaring whether the triangle is valid or not




     






