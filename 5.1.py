#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import grp
import glob
import platform

def main():

	#Creates a variable with the current user's name 
	#and user ID and prints them.
	name = os.getlogin()
	uid = os.getuid()
	print name+" "+str(uid)
	
	#Creates a list with the name of all groups in the 
	#grp.getgrall() module, which contains all groups
	#and all relevant information for the groups, by 
	#going through the list and checking for every line
	#(the g variable) if the name that we got earlier 
	#is in the groups members. 
	#No spaghetti here, sir!
	groups = [g.gr_name for g in grp.getgrall() if name in g.gr_mem]

	#And prints that list.
	print "Groups "+name+" is part of: "+str(groups)
	
	#Gets the current directory we're in (like pwd).
	loc = os.getcwd()
	print loc

	#Lists all the files in the current directory.
	files = os.listdir(loc)
	print files

	#Gets the operating system version.
	opsys = platform.platform()
	print opsys

	#Creates a dir called nymapp, in the current dir.
	create = os.mkdir("nymapp")

	#Creates a symolic link in nymapp.
	link = os.symlink("/dev/null","nymapp/mylink")

	#Changes the name of nymapp to nyaremapp.
	rename = os.rename("nymapp","nyaremapp")

	return 0


if __name__=='__main__':
	main()
