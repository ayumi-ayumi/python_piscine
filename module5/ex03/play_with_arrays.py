#!/usr/bin/env python3
original_arr = [2, 8, 9, 48, 8, 22, -12, 2]
new_arr = []

for num in original_arr:
	if (num > 5):
		new_arr.append(num + 2)

new_set = set(new_arr)

print(original_arr)
print(new_set)
