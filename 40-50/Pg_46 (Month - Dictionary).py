"""
WAP to create a dictionary whose keys are month names and whose values are the number of days in the corresponding month
i) Ask the user to enter a month name and use the dictionary to tell how many days are in the month
ii) Print out all of the keys in alphabetical order
iii) Print out all the of the months with 31 days
iv) Print out the (key-value) pairs sorted by the number of days in each month
"""
month_list = {"January": 31, "February": 28, "March": 31, "April": 30, "May": 31, "June": 30, "July": 31, "August": 31,
              "September": 30, "October": 31, "November": 30, "December": 31}
# i)
month_input = input("Enter a month (full name): ")
print("Number of days in ", month_input, "is ", month_list.get(month_input.strip(), "Enter again"))
# ii)
print(sorted(month_list))
# iii)
for i in month_list:
    if month_list[i] == 31:
        print("\n Month having 31 days are ", i, end=" ")
print()
# iv)
v = sorted([(i, j) for j, i in month_list.items()])
print("\n Sorted order is: ", [(j, i) for i, j in v])
