object1_x = int(input("Object #1's x component? "))
object1_y = int(input("Object #1's y component? "))
object2_x = int(input("Object #2's x component? "))
object2_y = int(input("Object #2's y component? "))

#asking the user the for the components of their x and y for different objects

xdistance = abs(object1_x - object2_x )
ydistance = abs(object1_y - object2_y )

#finding the distance between object 1 and object 2' x 

sq1 = object2_x - object1_x 
sq2 = object2_y - object1_y 


m = sq1 * sq1
m2 = sq2* sq2
m3 = m +m2

#finding the square root of the values to find the straihgt line distance

print("X distance = ", xdistance )
print("y distance = ", ydistance)
print("Straight line distance:" , m3**.5)

#printing the distances



