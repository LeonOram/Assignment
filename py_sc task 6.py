#Leon Oram
#21-09-2014
#py sc 6

import math

angle = 68
distance = 1.5

angle_rads = math.radians(angle)
height = math.tan(angle_rads) * distance

print("The ladder reaches {0}m heigh".format(height))
