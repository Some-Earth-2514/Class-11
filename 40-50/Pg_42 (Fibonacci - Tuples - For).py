# WAP that creates a tuple storing first "n" terms of a Fibonacci series. Value of "n" is inputted by user.
n = int(input("Enter number of terms in the fibonacci series: "))
a = 0
b = 1
l = [0, 1]
for x in range(1, n):
    c = a+b
    l.append(c)
    a = b
    b = c
t = tuple(l)
print(t)
