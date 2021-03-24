"""
Given a tuple namely car names as elements -

(toyota, honda, GM, Ford, BMW, Volkswagen, Mercedes, Ferrari, Porsche)

WAP to print names of the cars in the index range of 2 to 6 both inclusive

The output should also include the index in words as shown below:
    One         Honda
    Two         GM
"""
cars = ('toyota', 'honda', 'gm', 'ford', 'bmw', 'mercedes', 'ferrari', 'porshe')
car_pos = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven')
for a in range(2,7):
    print(car_pos[a], "\t", cars[a])
