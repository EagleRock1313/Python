# Load the Math Library (giving us access to math.pi and other values)
import math

# Ask for the radius of a circle that will be entered as a decimal number
radius = eval(input(("Enter the radius of the circle: ")))

# Computer circumference and area of this circle
circumference = 2 * math.pi * radius
area = math.pi * (radius ** 2)

# Results
print()
print("Circumference is", circumference)
print("Area is", area)
print("\nRounded: ")
print("Circumference is", round(circumference,2))
print("Area is", round(area,2))