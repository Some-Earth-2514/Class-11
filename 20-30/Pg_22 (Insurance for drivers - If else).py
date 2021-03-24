"""A company insures its driver in the following cases:
    If the driver is married
    If the driver is unmarried, male and above 30 yrs
    If the driver is unmarried, female and above 25 yrs
In all other cases, the driver is not insured. If the martial status , gender and age of the driver are the
inputs, WAP to determine whether the driver should be insured or not.
"""
Martial_S = input("Enter your martial status: m = married, u = unmarried ")
Gender = input("Enter your gender: m = male, f = female ")
Age = int(input("Enter your age "))
if Martial_S == "m":
    if Gender == "m" or Gender == "f":
        if Age >= 18:
            print("You are insured")
        else:
            print("You are not insured as it is illegal to be marry below the age of 18.")
    else:
        print("Invalid input")
elif Martial_S == "u":
    if Gender == "m":
        if Age > 30:
            print("You are insured")
        else:
            print("You are not insured")
    elif Gender == "f":
        if Age > 25:
            print("You are insured")
        else:
            print("You are not insured")
    else:
        print("Invalid input")
else:
    print("Invalid input")
