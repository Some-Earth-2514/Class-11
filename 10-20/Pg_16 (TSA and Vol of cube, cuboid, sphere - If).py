"""Write a menu driven program to calculate the total surface area and volume of a cube, cuboid, or sphere
depending upon user's choice"""
import math
print("1) Cube")
print("2) Cuboid")
print("3) Sphere")
choice = int(input("Enter the number of your choice "))
if choice == 1:
    side = int(input("Enter side value "))
    TSA = 6 * math.pow(side, 2)
    Vol = math.pow(side, 3)
    print("The total surface area = ", TSA, "and volume = ", Vol)
if choice == 2:
    length = int(input("Enter the length "))
    breadth = int(input("Enter the breadth "))
    height = int(input("Enter the height "))
    TSA = 2*((length*breadth)+(breadth*height)+(height*length))
    Vol = length * breadth * height
    print("The total surface area = ", TSA, "and volume = ", Vol)
if choice == 3:
    pi = 3.14
    radius = int(input("Enter the radius "))
    TSA = 4*pi*math.pow(radius, 2)
    Vol = 4/3*pi*math.pow(radius, 3)
    print("The total surface area = ", TSA, "and volume = ", Vol)
