#Leon Oram
#16-09-2014
#Stretch and challenge task 1

garden_length = int(input("Please enter the length of the garden in meters: "))
garden_width = int(input("Please enter the width of the garden in meters: "))

garden_area = (garden_length -1) * (garden_width - 1)
garden_cost = garden_area * 10

print("To turf the garden it will cost £{0} ".format(garden_cost))
