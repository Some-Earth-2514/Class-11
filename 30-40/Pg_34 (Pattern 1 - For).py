""" WAP a program to print the following:
1
1 3
1 3 5
1 3 5 7
4 3 2 1
4 3 2
4 3
4
"""
for a in range(1,8,2):
    for b in range(1,a+1,2):
        print(b, end=" ")
    print()

for i in range(1,5):
    for j in range(4,i-1,-1):
        print(j, end=" ")
    print()
