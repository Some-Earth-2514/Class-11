# WAP to input a number from the user and check if the given number is a prime or not
num = int(input("Enter a number "))
if num % 2 == 0:
    if num == 2:
        print("It is a prime")
    else:
        print("Not a prime")
elif num == 1:
    print("Not a prime")
else:
    print("It is a prime")
