# WAP to search for an element in a given list of numbers
a = eval(input("Enter a list of elements "))
b = int(input("Enter the number to be found "))
for i in range(0, len(a)):
    if b == a[i]:
        print(i, "position of the element")
        break
else:
    print("element not found")
