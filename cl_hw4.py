#!/usr/bin/env python3
"""Introduction to Computational Linguistics -- SS 2018 -- Assignment 4

Due: Thursday, 2018-07-22, 5:00 p.m.

Name : Annemarie Witschas, Marie Bensien, Emma Seeger
Tutor: Hannah Westerhagen 8
"""

import fileinput
import re

for line in fileinput.input():
	# we only need to consider tabulated lines (starting with a number), as these are the ones with the words and POS tags
	if re.match('[0-9]', line[0]):
		# makes a list out of the line splitting at the tabs
		wordlist = line.split("\t")

		# for each word of the text we print the POS tag
		print(wordlist[1], end="")
		print("_", end="")
		print(wordlist[3], end= " ")
