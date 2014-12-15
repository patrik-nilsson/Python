#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Import to get alphabet
import string

#Main finction that runs the findthem function. Also sends the arguments for the text to search through, and the alphabet.
def main():
	findthem("This is a string with some letters in it", list(string.ascii_lowercase))

#Receives the arguments and puts them in two variables.
def findthem(Astring, Alphabet):
	Letter={}
	for i1 in Astring:
		if i1 not in Letter:
			Letter[i1]=1
		else:
			Letter[i1]+=1
	print Letter
	return 0

if __name__=='__main__':
	main()
