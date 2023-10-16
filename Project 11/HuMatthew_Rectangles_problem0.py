class Rectangle:
    def __init__(self, width, length, x, y):
        self.width = width
        self.length = length
        self.x = x
        self.y = y

#calculates and returns the area of the rectangle

    def get_area(self):
        return self.length * self.width
    
#calculates and returns the perimeter of the rectangle

    def get_perimeter(self):
        return 2 * (self.length + self.width)


# Creates Rectangle #1
rect1 = Rectangle(10, 15, 5, 3)

# Creates Rectangle #2
rect2 = Rectangle(3, 5, 15, 7)

# Outputs the properties of the rectangles
print("Rectangle #1")
print(f"* Coordinates: ({rect1.x}, {rect1.y})")
print(f"* Area: {rect1.get_area()}")
print(f"* Perimeter: {rect1.get_perimeter()}")
print("Rectangle #2")
print(f"* Coordinates: ({rect2.x}, {rect2.y})")
print(f"* Area: {rect2.get_area()}")
print(f"* Perimeter: {rect2.get_perimeter()}")
