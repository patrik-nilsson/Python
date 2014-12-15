#!/usr/bin/env python
# -*- coding: utf-8 -*-
import locale

def main():
	#Receive input from user
	print "Enter a number:"
	s=input(">")
	#Set checks to see if it's an int or float
	d="<type 'int'>"
	f="<type 'float'>"
	#Start spacing function
	spacing(s,d,f)

def spacing(s,d,f):
	#Unnecessary variables
	x=","
	y=" "
	z="."
	#Sets the locale for all categories to the user's default setting. Basically, sets the language settings.
	locale.setlocale(locale.LC_ALL, '')
      	#checks if it's an int
        if isinstance(s, int):
		#Puts comma as a thousand seperator 
		r="{:,}".format(s)
		#Replace comma with spaces
		r=r.replace(x,y)
		#return the number
		return r
	#checks if it's a float
        elif isinstance(s, float):
		#only keep two decimals
		s=("%.2f" %s)
		#Puts comma as a thousand seperator
		r="{:,}".format(float(s))
		#replace comma with spaces
		i=r.replace(x,y)
		#replace dot with a comma.
		i=i .replace(z,x)
		#return the number
		return i
	#If it's neither an int nor float...
        else:
		#Return empty string.
                return ""

if __name__=='__main__':
	main()
