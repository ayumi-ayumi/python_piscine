#!/usr/bin/env python3
text = input()
# i = 0
# while i < len(text):
# 	if (text[i].islower()):
# 		print(text[i].upper(), end="")
# 	else:
# 		print(text[i].lower(), end="")
# 	i += 1;
for char in text:
	if (char.islower()):
		print(char.upper(), end="")
	else:
		print(char.lower(), end="")
