"""Sonia has to travel a distance of 450km by car.From her experience she knows that she will be travelling at a
certain average speed. WAP to find out how much time she will take to cover the distance"""
print("""Sonia has to travel a distance of 450km by car.From her experience she knows that she will be travelling at a
certain average speed. Input the average speed so as to find out how much time she will take""")
distance = 450
average_speed = float(input("Average speed in km's = "))
time = (distance/average_speed)
print("Time taken by her = ", time, "hrs")
