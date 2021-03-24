"""WAP to input a number and the no. of multiples from the KB and display the multiplication table of the
given number"""
num = int(input("Enter a number "))
multiples = int(input("Enter the number of multiples "))
for multiples in range(1, multiples+1):
    prod = num * multiples
    print(num, "x", multiples, "=", prod)
