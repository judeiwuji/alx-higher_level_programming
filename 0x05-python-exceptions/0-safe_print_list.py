#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
	len = 0
	for i in range(0, x):
		try:
			print("{}".format(my_list[i]), end="")
			len += 1
		except:
			break
	print()
	return len
