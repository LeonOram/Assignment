
age = int(input("Please enter your age: "))
if age >= 18:
    print("You are old enough to vote!")
else:
    print("You are not old enough to vote.")
y2r = 65 - age
print("Only {0} years until you can retire!".format(y2r))
