#Leon Oram
#21-09-2014
#py sc 5

import math
angle = 1
distance = 1000
angle_rads = math.radians(angle)

ver_height = math.sin(angle_rads) * distance

print("the vertical distance traveled is {0} meters".format(ver_height))
