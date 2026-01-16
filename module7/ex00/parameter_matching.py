#!/usr/bin/env python3
import sys
av_list = sys.argv
av_list_len = len(av_list)
if (av_list_len == 2):
	input_word = input("What was the parameter? ")
	word = av_list[1];
	if (input_word == word):
		print("Good job!")
	else:
		print("Nope, sorry...")
else:
	print("none")
