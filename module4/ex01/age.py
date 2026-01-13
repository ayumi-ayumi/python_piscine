#!/usr/bin/env python3
age = input("Please tell me your age: ")
print(f"You are currently {age} years old.")
age_num = int(age)
for i in range(10, 31, 10):
	print(f"In {i} years, you'll be {age_num + i} years old.")
