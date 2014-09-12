#Leon Oram
#12-09-2014
#Dev task 3

height_inch = float(input("Please enter your height in inches:"))
weight_stone =float(input("Please enter your weight in stones:"))

height_centi = height_inch *2.54
weight_kilo = weight_stone * 6.364

print("Your height is {0} centimeters and your weight is {1} kilograms".format(height_centi,weight_kilo))
