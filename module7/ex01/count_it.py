#!/usr/bin/env python3
import sys
av_list = sys.argv
av_list_len = len(av_list)
if (av_list_len > 2):
	print(f"parameters: {av_list_len - 1}")
	for i in range(1, av_list_len):
		print(f"{av_list[i]}: {len(av_list[i])}")
else:
	print("none")
