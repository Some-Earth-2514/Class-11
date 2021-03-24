"""WAP to input a set of positive and negative numbers from the user. The program continues to take input as long
as the user wants to input values. At the end, the program must display the sum of positive and negative numbers
separately.
"""
yn = "y"
psum = 0
nsum = 0
while yn == "y":
    pos = int(input("Enter a positive number:"))
    if pos < 0:
        print("Number is negative")
    neg = int(input("Enter a negative number:"))
    if neg > 0:
        print("Number is positive")
    nsum += neg
    psum += pos
    yn = input("Continue? (y/n)")
print("The sum of positive numbers is ", psum, "and the sum of negative numbers is ", nsum)
