"""WAP that inputs 3 numbers and calculates 2 sums as per the following condition:
sum1 as the sum of all input numbers
sum2 as the sum of non-duplicate numbers, if there are duplicate numbers in the input, ignore them"""
print("Enter 3 numbers")
num1 = int(input())
num2 = int(input())
num3 = int(input())
sum1 = (num1 + num2 + num3)
print("The sum of the numbers = ", sum1)
if (num1 == num2) or (num2 == num3) or (num3 == num1):
    print("Please input 3 DIFFERENT numbers")
else:
    sum2 = (num1 + num2 + num3)
    print("The sum of the numbers = ", sum2)
