""" WAP that
1. prompts the user for a string
2. extracts all the digits from the string
3. if there are digits:
   sum the collected digits together
   print out:
   original string
   digits
   sum of the digits
If there are no digits:
   print the original string and a message  "has no digits"
"""
string = input("Enter a string ")
print(string)
sum1 = 0
for a in string:
    if a.isdigit():
        sum1 += int(a)
        print(a)
if sum1 == 0:
    print("has no digits")
else:
    print(sum1)
