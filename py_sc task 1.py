#Leon Oram
#16-09-2014
#py_sc task 1

import math

radius = float(input("Please enter the radius of the circle: "))

circumf = math.pi * (radius*2)
area = math.pi * (radius**2)

print("The circumfrence of the circle is {0:.2f}".format(circumf))
print("The area of the circle is {0:.2f}".format(area))
