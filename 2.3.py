#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

""" In the main function
	-sets variables for use in gameend
	-randomises a number
	-initiates the gamestart function
"""
def main():
	c="Correct"
	w="Wrong"
	r=random.randrange(1,11)
	gamestart(r, c, w)
	return 0

""" In the gamestart function
	-asks the user for a number
	-grabs the input
	-checks if it's correct, higher or lower
	-gives you another try if you're wrong
	-initiates the gameend function
"""
def gamestart(n, c, w):
	print "Guess a number from 1 to 10. You get 2 attempts."
	g=input(">")
	for i in (1,2):
		if g == n:
			a=c
			break
		elif g < n:
			print "Wrong! "+str(g)+" is lower!"
			print "Guess a higher number!"
			a=w
		elif g > n:
			print "Wrong! "+str(g)+" is higher!"
			print "Guess a lower number!"
			a=w
		if i < 2:
			g=input(">")
	gameend(n, a, c, w)

""" In the gameend function
	-checks if the answer was correct or wrong
	-when done, returns to main function
"""
def gameend(n, a, c, w):
	if a == c:
		print "Correct! "+str(n)+" was the correct number!"
	elif a == w:
		print "You couldn't guess the number.. It was "+str(n)

if __name__=='__main__':
	main()
