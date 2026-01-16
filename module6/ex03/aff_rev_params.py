#!/usr/bin/env python3
import sys
av_list = sys.argv
av_list_len = len(av_list)
if av_list_len <= 2:
	print("none")
else:
	while av_list_len > 1:
		print(f"{av_list[av_list_len - 1]}")
		av_list_len -= 1
