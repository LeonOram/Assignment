#Leon Oram
#16-09-2014
#py_sc task 2

import math

pool_diameter = float(input("Please enter the diameter of the pool: "))
pool_depth = float(input("Please enter the depth of the pool: "))

pool_volume = (math.pi * (pool_diameter/2)**2) * pool_depth

print("The volume of the pool is {0}".format(pool_volume))
