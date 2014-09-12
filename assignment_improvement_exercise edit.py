#john bain
#variable improvement exercise
#05-09-12

import math

radius = float(input("please enter the radius of the circle: "))

circumf = 2* math.pi * radius
circumf = round(circumf,2)

area = math.pi * radius**2
area = round(area,2)

print("The circumference of this circle is {0}.".format(circumf))
print("The area of this circle is {0}.".format(area))
