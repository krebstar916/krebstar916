#!/usr/bin/python3
import ipaddress
import random

def genip():
	done = 0
	while done == 0:
		output = random.randint(0,4294967295)
		if output == 0:
			print(".", end="")
			done = 0
		elif (167772160 < output) & (output < 184549375):
			print(".", end="")
			done = 0
		elif (2886729728 < output) & (output < 2886795263):
			print(".", end="")
			done = 0
		elif (3232235520 < output) & (output < 3232301055):
			print(".", end="")
			done = 0
		elif (2851995648 < output) & (output < 2852061183):
			print(".", end="")
			done = 0
		elif (output == 4294967295):
			print(".", end="")
			done = 0
		else:
			publicaddr = str(ipaddress.ip_address(output))
			done = 1 
	return publicaddr

