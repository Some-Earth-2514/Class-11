"""
WAP to read a list containing 3 digit integers only. Then write a sort prg that sorts the list on the basis of one's
digit of all the elements.
Eg - [387, 410, 285, 106]
     [410, 285, 106, 387]
"""
inp_list = eval(input("Enter a list of 3 digit numbers "))
length = len(inp_list)
print("List before sorting: ", inp_list)
for i in range(1, length):
    temp = inp_list[i] % 10
    t = inp_list[i]
    j = i-1
    while j >= 0 and temp < (inp_list[j] % 10):
        inp_list[j+1] = inp_list[j]
        j = j - 1
    inp_list[j+1] = t
print("List after sorting: ", inp_list)
