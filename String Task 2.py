#Leon Oram
#06-10-2014
#String Task 2

string = input("Please enter your quote: ")
replace = input("Please input word to replace: ")
replace_with = input("Please input what will replace the specified: ")

string = string.replace(replace,replace_with)
upper = string.upper()
lower = string.lower()
caps = string.capitalize()
title = string.title()

print("{0}: {1}: {2}: {3}".format(upper,lower,caps,title))
