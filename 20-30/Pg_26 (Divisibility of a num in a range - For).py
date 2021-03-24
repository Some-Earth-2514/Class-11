"""WAP to print every integer 1 to "n" to see if it is divisible by "m". Also report whether the number that
is divisible by "m" is even or odd"""
n = int(input("Enter a number (upper limit of the range) "))
m = int(input("Enter a number to see if the previous number is divisible by it "))
for a in range(1, n+1):
    if a % m == 0:
        if a % 2 == 0:
            print(a, "is even and divisible by", m)
        else:
            print(a, "is odd and divisible", m)
