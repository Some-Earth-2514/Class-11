"""WAP to input numbers from the keyboard and find the sum of the numbers and display them. The program should
continue to take input from the user as long as the number "0" is not entered by the user."""
num = int(input("Enter a number (to exit enter 0) "))
sum1 = 0
while num > 0:
    sum1 += num
    num = int(input("Enter a number (to exit enter 0) "))
print("Sum = ", sum1)
