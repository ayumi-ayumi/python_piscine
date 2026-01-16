#!/usr/bin/env python3
import sys
av_list = sys.argv
av_list_len = len(av_list)
if (av_list_len != 1):
	print(av_list[1].lower())
else:
	print("none")
