#!/usr/bin/env python3
import sys
av_list = sys.argv
av_list_len = len(av_list)

def shrink(str):
	return str[:8]
	
def enlarge(str):
	for i in range(len(str), 8):
		str += 'Z'
	return str

if av_list_len == 1:
	print("none")
else:
	for i in range(1, av_list_len):
		target = av_list[i]
		if len(target) > 8:
			print(shrink(target))
		elif len(target) < 8:
			print(enlarge(target))
		else:
			print(target)
