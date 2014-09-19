#Leon Oram
#19-09-2014
#We need ifs

amount = int(input("Please enter the amount:"))

amount_20s = amount // 20
amount = amount % 20
amount_10s = amount // 10
amount = amount % 10
amount_5s = amount // 5
amount = amount % 5
amount_2s = amount // 2
amount = amount % 2
amount_1s = amount // 1
amount = amount % 1

print("The number of notes/coins is : £20s {0}, £10s {1},£5s {2}, £2s{3},£1s {4}".format(amount_20s,amount_10s,amount_5s,amount_2s,amount_1s))
