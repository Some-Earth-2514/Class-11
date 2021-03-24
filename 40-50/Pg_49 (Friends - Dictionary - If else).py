friends = int(input("Enter the number bigger than 5: "))
phone_dict = {}
if friends < 5:
    print("Please enter a number bigger than 5")
elif friends >= 5:
    for a in range(0, friends):
        f_name = input("Enter the friend's name: ")
        f_num = input("Enter the friend's ph. num: ")
        phone_dict[f_name] = f_num
print("The product dictionary is: ")
print(phone_dict)