#Leon Oram
#12-09-2014
#Dev task 4

pool_length = float(input("Please enter the length of the pool in meters:"))
pool_width = float(input("Please enter the width of the pool in meters:"))
pool_deepest = float(input("Please enter the depth of the deepest point of the pool in meters:"))
pool_shallowest = float(input("Please enter the depth of the shallowest point of the pool in meters:"))
pool_ave_depth = (pool_deepest + pool_shallowest) / 2
pool_volume_cmet = pool_length * pool_width * pool_ave_depth
pool_volume_litres = pool_volume_cmet * 1000
print("The total volume of the pool is {0} cubic meters or {1} litres".format(pool_volume_cmet,pool_volume_litres))
