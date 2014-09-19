#Leon Oram
#18-09-2014
#Denary to Hex

denary = int(input("Please enter your denary number: "))

binary = ""
if denary == 0:
    print("The binary value is 0")
else:
    while denary > 0:
        binary = str(denary % 2) + binary
        denary = denary // 2

    print("the binary value is {0}".format(binary))

total_length = len(binary)

print(total_length)

length = total_length
while length > 0:
    if length > 4:
        binary segment = binary[0:4]
        binary = binary_segment [:-4]
    else:
        binary_segment = binary[0:length]

