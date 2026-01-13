#!/usr/bin/env python3
num = float(input("Give me a number: "))
if (num * 10) % 10 != 0:
	print("This number is a decimal.")
else:
	print("This number is an integer.")
