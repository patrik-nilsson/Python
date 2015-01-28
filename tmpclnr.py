#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, time, sys

def main():
	filesremoved=0 #Counter for num. of removed files.
	path=r"/tmp" #Path to the top of the tree to clean.
	now=time.time() #The current time in a variable.

	for root, dirs, files in os.walk(path,topdown=False):
	#Loop going through all the files and directories from bottom to top

		d=str(root) #Var for the current Dir the program is going through
		for f in files: #Loop through the files in the Dir
			newpath=d+"/"+f #Var for full path to the file

			if os.stat(newpath).st_mtime < now - 86400*30: 
			#If the file's not been touched for a month

				if os.path.isfile(newpath):
				#and If the path is a file.

					try: #Attempt to remove the file
						os.remove(newpath)
						#Announce the removed file
						print "Removed "+newpath
						#and Add to counter
						filesremoved+=1

					#In case the file couldn't be removed.
					except:
						#Do nothing.
						False
	#Print the num. of removed files.
	print "%d files were removed." %filesremoved

	return 0

if __name__=='__main__':
	main()
