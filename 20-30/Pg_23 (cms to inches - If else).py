"""WAP to that asks the user to enter the length in centimetres. If the user enters a negative number length the
program should tell user that the entry is invalid. Otherwise, the program should convert the length to inches
and print the result.
1 inch = 2.54 cm
"""
num = float(input("Enter length in cm "))
if num < 0:
    print("Invalid input")
else:
    num = num * 2.54
    print("Length in inches = ", num)
