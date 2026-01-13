#!/usr/bin/env python3
first_num = input("Enter the first number: ")
second_num = input("Enter the second number: ")
multi = int(first_num) * int(second_num)
# print(str(first_num) + " x " + str(second_num) + " = " + str(multi))
print(f"{first_num} x {second_num} = {multi}")

if multi == 0:
	print("The result is positive and negative.")
elif multi < 0:
	print("The result is negative.")
else:
	print("The result is positive.")
