#!/usr/bin/env python3
original_arr = [2, 8, 9, 48, 8, 22, -12, 2]
modi_arr = []
i = 0;
# while i < len(original_arr):
for num in original_arr:
	if (num > 5):
		modi_arr.append(num + 2)

print(f"Original array: {original_arr}")
print(f"New array: {modi_arr}")
