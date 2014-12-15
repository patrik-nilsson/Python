#!/usr/bin/env python
# -*- coding: utf-8 -*-
import shutil
import sys
import os

def main():
		#Checks if the argument is a directory
		if os.path.isdir(sys.argv[1]):
			#Checks if /tmp/backup exists
			if os.path.isdir("/tmp/backup"):
				#If it does, it can't do anything...
				print "Directory /tmp/backup/ already exists!"
			else:
				#Else, it creates a backup of the selected directory
				shutil.copytree(sys.argv[1],"/tmp/backup",symlinks=False, ignore=None)
		#Checks if the argument is a file
		elif os.path.isfile(sys.argv[1]):
			#Checks if the /tmp/backup exists
			if os.path.isdir("/tmp/backup"):
				#If it does, it creates a backup file in /tmp/backup/
				shutil.copy2(sys.argv[1],"/tmp/backup/"+sys.argv[1])
			else:
				#Else, it creates /tmp/backup, and a backup file in it.
				os.mkdir("/tmp/backup")
				shutil.copy2(sys.argv[1],"/tmp/backup/"+sys.argv[1])
		#Checks if you asked to delete the backup folder, and if so; does it.
		elif sys.argv[1]=="Delete" or sys.argv[1]=="delete":
			try:
				shutil.rmtree("/tmp/backup")
			except OSError:
				print "There is no backup!"
		#If the argument didn't seem to exist as a file or directory; say so, and how to use this app..
		else:
			print """That is not a file or directory!
Usage: 5.1.py [file/directory]
5.2.py lets you create a backup in /tmp/backup.
You can also delete the backup by using the argument delete/Delete."""
		return 0

if __name__=='__main__':
	main()
