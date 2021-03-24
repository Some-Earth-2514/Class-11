# WAP to find the roots of a quadratic equation
import math
print("Enter 3 numbers")
a = int(input())
b = int(input())
c = int(input())
d = ((math.pow(b, 2))-(4*a*c))
if d >= 0:
    x = (-b+(math.sqrt(d)))/2*a
    y = (-b-(math.sqrt(d)))/2*a
else:
    x = complex((-b/(2*a)), math.sqrt(-d)/(2*a))
    y = complex((-b/(2*a)), -math.sqrt(-d)/(2*a))
if d > 0:
    print("THe function has 2 distinct real roots: ", x, y)
elif d == 0:
    print("The function has 1 double root ", x)
else:
    print("Th function has 2 complex roots: ", x, ",", y)
