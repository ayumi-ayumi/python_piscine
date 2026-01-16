#!/usr/bin/env python3
import sys
import re
av_list = sys.argv
av_list_len = len(av_list)
if (av_list_len > 2):
	word = av_list[1];
	str = av_list[2];
	count = len(re.findall(word, str))
	if count >= 1:
		print(count)
	else:
		print("none")
else:
	print("none")
