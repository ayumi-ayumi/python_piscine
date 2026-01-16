#!/usr/bin/env python3
import sys
av_list = sys.argv
av_list_len = len(av_list)
if (av_list_len > 1):
	for i in range(1, av_list_len):
		has_ism = av_list[i].find("ism")
		if (has_ism == -1):
			print(f"{av_list[i]}ism")
else:
	print("none")
