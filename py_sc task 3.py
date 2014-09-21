#Leon Oram
#21-09-2014
#py sc 3

import math

distance = int(input("please enter the distance traveled: "))
angle = int(input("please enter the bearing: "))

angle_rad = math.radians(angle)
#North
north_dist = math.cos(angle_rad) * distance

#East
east_dist = math.sin(angle_rad) * distance

print("Traveled {0}km north and {1}km east".format(north_dist,east_dist))
