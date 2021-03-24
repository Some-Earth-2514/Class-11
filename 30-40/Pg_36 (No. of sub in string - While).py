""" WAP that reads a line and a substring. It should then display the number of occurrences of the given substring in
the line."""
string = input("Enter a string ")
substring = input("Enter a substring ")
len_str = len(string)
len_sub = len(substring)
start = count = 0
end = len_str
while True:
    position = string.find(substring, start, end)
    if position != -1:
        count += 1
        start = position + len_sub
    else:
        break
    if start >= len_str:
        break
print("The number of times", substring, "is present in", string, "=", count)
