# WAP to sum the sequence: 1+1/1!+1/2!+1.../n!+1 (factorial)
num = int(input("Enter a number "))
sum_ = 1
factorial = 1
for num in range(1, num + 1):
    factorial = num * factorial
    sum_ = sum_ + 1 / factorial
print("Sum of the series is = ", sum_)
