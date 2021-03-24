"""WAP that prompts for a phone number of a 10 digits and 2 dashes, with dashes after the area code and the
next 3 numbers. Display if the phone is valid format or not and display if the phone number is valid or not
(contains just the digits and dashes at specific places).
Eg - 999-999-9999
"""
number = input("Enter a phone number, 999-999-9999 ")
if len(number) == 12 and number[3] == "-" and number[7] == "-":
    if number[0:3].isdigit() and number[4:7].isdigit() and number[8:13].isdigit():
        print("Phone number is valid")
    else:
        print("Input is invalid")
else:
    print("Input is invalid")
