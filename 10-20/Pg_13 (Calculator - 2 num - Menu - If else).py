"""WAP that reads two numbers and an arithmetic operator and displays the completed result.
Menu on screen
1) Enter first number
2) Enter second number
3) Enter an operator
"""
num1 = float(input("Enter a big number "))
num2 = float(input("Enter a number smaller than the previous one "))
operator = input("Enter an operator [+-/*] ")
sum1 = num1 + num2
diff = num1 - num2
quotient = num1 / num2
product = num1 * num2
if operator == "+":
    print("The sum is = ", sum1)
elif operator == "-":
    print("The difference is = ", diff)
elif operator == "/":
    print("The quotient is = ", quotient)
elif operator == "*":
    print("The product is = ", product)
else:
    print("Invalid input")
