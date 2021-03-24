# The three sides of a triangle are entered through the keyboard. WAP to check if the triangle is valid
s1 = int(input("Enter first side "))
s2 = int(input("Enter second side "))
s3 = int(input("Enter third side "))
if (s1 + s2 > s3) or (s1 + s3 > s2) or (s2 + s3 > s1):
    print("Valid triangle")
else:
    print("Invalid triangle")
