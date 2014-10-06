num = int(input("Please enter a number between 1 and 20: "))
if num >= 1 and num <= 20:
    print("That number is within the range")
elif num < 1:
    print("That number is too low")
elif num > 20:
    print("That number is too high")
