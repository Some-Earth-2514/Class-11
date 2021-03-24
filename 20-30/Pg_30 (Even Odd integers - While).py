# WAP to display sum of even and odd integers of the first "n" natural numbers.
n = int(input("Enter a number for the upper limit "))
control = 1
sum_even = 0
sum_odd = 0
while control <= n:
    if control % 2 == 0:
        sum_even += control
    else:
        sum_odd += control
    control += 1
print("Sum of even integers = ", sum_even)
print("Sum of odd integers = ", sum_odd)
