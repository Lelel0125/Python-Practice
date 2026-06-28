# Exercise 1 circumference of circle
## import math

## radius = float(input("Enter the radius of a circle: "))

## circumference = 2 * math.pi * radius

## print(f"The circumference is: {round(circumference, 2)}cm")

# Exercise 2 Area of circle
## import math

## radius = float(input("Enter the radius of a circle: "))

## area = math.pi * pow(radius, 2)

## print(f"The area of the circle is: {round(area, 2)}cm^2")

#Exercise 3 Hypotenuse calc of Right triangle
import math

a = float(input("Enter sid A: "))
b = float(input("Enter sid B: "))

c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"Side C = {c}")