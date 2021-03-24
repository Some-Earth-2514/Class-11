"""
Input a list of ‘L’ elements from the user. Multiply an element by 2 if its odd index. Display the final list.
Also find and display the sum of all the values which are ending with 3 from the original list.
"""
L = int(input("Enter number of elements: "))
list1 = []

for i in range(1, L + 1):
    b = int(input("Enter an element: "))
    list1.append(b)
new_list = list1

for j in range(len(list1)):
    if j % 2 != 0:
        new_list.append(list1[j] * 2)
print("The new list is ", new_list)
sum1 = 0

for k in list1:
    if k % 10 == 3:
        sum1 += k
print("Sum of all numbers ending with 3 is: ", sum1)
