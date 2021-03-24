# WAP that contains a tuple T and displays the second largest element in the tuple
list1 = eval(input("Enter a list (put [] around your list): "))
list.sort(list1)
tuple1 = tuple(list1)
print(tuple1, "is the tuple")
print("The second largest number is ", list1[-2])
