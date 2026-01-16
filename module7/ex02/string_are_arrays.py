#!/usr/bin/env python3
import sys
av_list = sys.argv
av_list_len = len(av_list)
if (av_list_len == 2):
	char = 'z';
	str = av_list[1];
	count = 0
	for i in str:
		if (i == char):
			count += 1
			print("z", end="")
	if count == 0:
			print("none")
else:
	print("none")
