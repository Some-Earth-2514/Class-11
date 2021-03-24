# WAP to input a number from the user, if the number is odd and positive print its square root otherwise print its cube
import math
num = int(input("Enter a number "))
if num % 2 == 0:
    print("Its cube is = ", math.pow(num, 3))
else:
    print("Its square root is = ", math.sqrt(num))
