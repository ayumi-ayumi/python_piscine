#!/usr/bin/env python3
original_arr = [2, 8, 9, 48, 8, 22, -12, 2]
new_arr = []
for num in original_arr:
	if (num > 5):
		new_arr.append(num + 2)

print(f"Original array: {original_arr}")
print(f"New array: {new_arr}")
