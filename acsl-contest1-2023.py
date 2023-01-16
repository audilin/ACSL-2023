#!/bin/python3

import math
import os
import random
import re
import sys
import lists



#
# Complete the 'findModeCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER num
#  2. INTEGER base
#  3. STRING start
#

def getIndex(baseDigits, digit):
	for i in range(0, len(baseDigits)):
		if (baseDigits[i] == digit):
			return i

		

def nextNum(current, base): # current is string, base is int
	digits = ["0","1","2","3","4","5","6","7","8","9","A", "B", "C", "D", "E", "F"]
	baseDigits = digits[:base]
	if(base == 16): baseDigits = digits.copy
	result = ""
	length = len(current)
	
	#add 1 to last digit
	roundUp = False
	lastCharacter = getIndex(baseDigits, current[-1]) + 1 # baseDigits.index(current[-1]) + 1
	current = current[:-1]
	if(lastCharacter>= base):
		roundUp = True
		lastCharacter = lastCharacter - base
	result = baseDigits[lastCharacter] + result
	length = length - 1
	
	#see if other digits need to be rounded up
	while(length > 0):
		lastCharacter = getIndex(baseDigits, current[-1])
		current = current[:-1]
		if(roundUp):
			lastCharacter = lastCharacter + 1
			roundUp = False
		if(lastCharacter + 1 >= base):
			roundUp = True
			lastCharacter = lastCharacter - base
			
		result = baseDigits[lastCharacter] + result
		length = length - 1
	if(current == "" and roundUp):
		result = "1" + result
	return result

def countDigits(allDigits, digit): # both inputs are strings
	count = 0
	for character in allDigits:
		if character == digit:
			count = count + 1
	return count

def findModeCount(num, base, start):
	digits = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #16 zeroes
	allDigits = start # will store all numbers
	current = start
	for n in range(1, num):
		next = nextNum(current, base)
		allDigits = allDigits + next
		current = next
	
	# print(allDigits)
	bestDigit = 0
	bestCount = 0
	for n in range(0,10):
		digits[n] = countDigits(allDigits, str(n))
		if digits[n] > bestCount:
			bestCount = digits[n]
			bestDigit = n
		
	
	digits[10] = countDigits(allDigits, "A")
	digits[11] = countDigits(allDigits, "B")
	digits[12] = countDigits(allDigits, "C")
	digits[13] = countDigits(allDigits, "D")
	digits[14] = countDigits(allDigits, "E")
	digits[15] = countDigits(allDigits, "F")
	for n in range(10,16):
		if digits[n] > bestCount:
			bestCount = digits[n]
			bestDigit = n
	
	return bestCount

def main():
	num = 5
	base = 16
	start = "ABC"

	print(findModeCount(num, base, start))
	# allDigits = ""
	# current = start
	# for n in range(0, num):
	# 	next = nextNum(current, base)
	# 	allDigits = allDigits + next
	# 	print(next)
	# 	current = next
	# print(nextNum("177777777", 9))

if __name__=="__main__":
	main()
