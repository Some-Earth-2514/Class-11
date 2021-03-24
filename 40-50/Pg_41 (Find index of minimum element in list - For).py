# WAP to find minimum element from a list of elements along with its index in the list
list1 = eval(input("Enter a list of numbers: "))
length = len(list1)
element = int(input("Enter the element you would like to search for: "))
for i in range(0, length):
    if element == list1[i]:
        print(element, "found at index", i)
        break
else:
    print(element, "not found in the list")
min_element = list1[0]
min_index = 0
for i in range(1, length):
    if list1[i] < min_element:
        min_element = list1[i]
        min_index = i
print("List is: ", list1)
print("The minimum element in the list is ", min_element, "found at index ", min_index)
