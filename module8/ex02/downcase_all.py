#!/usr/bin/env python3
import sys

av_list = sys.argv
av_list_len = len(sys.argv)

def downcase_it(str):
	return str.lower()

if av_list_len != 1:
	for av in av_list:
		print(downcase_it(av))
else:
	print("none")
