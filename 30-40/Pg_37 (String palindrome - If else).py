# WAP that reads a string and checks whether it is a palindrome string or not.
string = input("Enter a string ")
if string == string[::-1]:
    print(string, "is a palindrome")
else:
    print(string, "is not a palindrome")
