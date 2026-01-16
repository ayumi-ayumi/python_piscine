#!/usr/bin/env python3
import sys
av_list = sys.argv
av_list_len = len(av_list)
if (av_list_len == 3):
	first_num = int(av_list[1])
	second_num = int(av_list[2])
	arr = []
	if (first_num < second_num):
		for i in range(first_num, second_num + 1):
			arr.append(i)
		print(arr)
	else:
		print("none")
else:
	print("none")
