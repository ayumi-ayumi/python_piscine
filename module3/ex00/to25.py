#!/usr/bin/env python3
input_num = int(input("Enter a number less than 25\n"))
if input_num > 25:
	print("Error")
else:
	i = input_num
	while i <= 25:
		print(f"Inside the loop, my variable is {i}")
		i += 1

	# for num in range(20, 25 + 1):
	# 	print(f"Inside the loop, my variable is {num}");
