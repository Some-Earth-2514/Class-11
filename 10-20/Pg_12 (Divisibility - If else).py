# WAP to test the divisibility of a number with another number
num1 = int(input("Enter a big number "))
num2 = int(input("Enter a number smaller than the previous one "))
quotient = num1 % num2
if quotient == 0:
    print("The numbers are divisible")
else:
    print("Then numbers are not divisible")
