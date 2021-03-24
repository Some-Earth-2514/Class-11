""" WAP that repeatedly asks the user to enter the product names and prices.
Store all of these in a dictionary whose keys are the product names and whose values are the prices."""
number = int(input("Enter the number of products "))
product_dict = {}
for a in range(0, number):
    p_name = input("Enter the product names ")
    p_price = input("Enter the product price ")
    product_dict[p_name] = p_price

print("The product dictionary is: ")
print(product_dict)
p_name1 = input("Enter the product name to view price ")
print(product_dict[p_name1])
