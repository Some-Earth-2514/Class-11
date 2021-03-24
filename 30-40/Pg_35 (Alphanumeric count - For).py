"""WAP that reads a line prints its statistic like:
Number of uppercase letters:
Number of lowercase letters:
Number of alphabets:
Number of digits:
"""
string = input("Enter a alphanumeric string ")
Up_count = Low_count = Alpha_count = Digi_count = Spl_count = 0
for a in string:
    if a.isalpha():
        Alpha_count += 1
    if a.islower():
        Low_count += 1
    if a.isupper():
        Up_count += 1
    if a.isdigit():
        Digi_count += 1
    else:
        Spl_count += 1
print("Number of uppercase letters = ", Up_count)
print("Number of lowercase letters = ", Low_count)
print("Number of alphabets = ", Alpha_count)
print("Number of digits = ", Digi_count)
