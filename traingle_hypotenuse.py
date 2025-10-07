import math

p = float(input("Enter length of perpendicular in cm: "))
b = float(input("Enter length of base in cm: "))
h = math.sqrt(pow(p, 2) + pow(b, 2))

print(f"The length of hypotenuse is {round(h, 2)} cm")
