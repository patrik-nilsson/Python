#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Import to get alphabet
import string

#Main finction that runs the findthem function. Also sends the arguments for the text to search through, and the alphabet.
def main():
	findthem("this is a string with some letters in it", list(string.ascii_lowercase))

#Receives the arguments and puts them in two variables.
def findthem(Astring, Alphabet):
	#Define list to put the letter it's amount in.
	Letter={}
	#Goes through the Alphabet, letter for letter.
	for i1 in Alphabet:
		#Reset i3 for every letter.
		i3=0
		#Search through the string for the assigned letter.
		for i2 in Astring:
			#If a letter is matching, it adds 1 to i3.
			if i1 == i2:
				i3+=1
		#If a letter was found, it adds a value to it, and prints it out.
		if i3>0:
			Letter[i1]=i3
			print i1+" "+str(Letter[i1])
	return 0

if __name__=='__main__':
	main()
