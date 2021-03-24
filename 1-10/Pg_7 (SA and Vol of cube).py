# Calculate surface area and volume of a cube and get input from user.
import math
side = int(input("Enter the length of the cube "))
surface_area = 6 * (math.pow(side, 2))
volume = (math.pow(side, 3))
print("Surface area of the cube is ", surface_area)
print("Volume of the cube is ", volume)
