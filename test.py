#!/usr/bin/env python
# -*- coding: utf-8 -*-
import operator
import sys

def main():
	#Create line counter
	lcounter=0
	#Make sure the file can be opened.
		#Opens the file during the following tasks and put it's content in the variable f.
	with open(sys.argv[1]) as f:
			#Read each line from the file per loop.
		for line in f:
				#add 1 to line counter and put word counter to 0
			lcounter+=1
			wcounter=0
				#Split the lines into words
			for word in line.split():
					#add 1 to word counter
				wcounter+=1
					#Remove any special characters
				a=word.lower().replace('"','').replace(',','').replace('.','').replace('!','').replace('?','').replace(':','').replace(';','')
					#If the word we're looking for is found, print row, position of the word and the entire line in which the word is.
				if word == sys.argv[2]:
					print "Line: "+str(lcounter)+" Position: "+str(wcounter)
					print line

	return 0

if __name__=='__main__':
	main()
