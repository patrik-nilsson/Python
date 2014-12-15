#!/usr/bin/env python
# -*- coding: utf-8 -*-
import my_module

def main():
	print "How old are you?"
	a=input(">")
	print "What month were you born?"
	print "Answer with a number Ex. January = 1"
	m=input(">")
        print "What day of the month were you born?"
        print "Ex. 25"
	d=input(">")
	r=my_module.bornyear(m,d,a)
	print "You were born "+str(r)+"!"
	return 0

if __name__=='__main__':
	main()
