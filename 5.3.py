#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import time
import sys
def thedate(getdate):
	year=''
	month=getdate[0:3]
	month=time.strptime(month,'%b').tm_mon
	day=getdate[4:6]
	hour=getdate[7:9]
	minute=getdate[10:12]
	second=getdate[13:15]
	return (str(month)+" "+str(day)+" "+str(hour)+":"+str(minute)+":"+str(second))
	
def main():
	indate=input("Date: ")
	indate=indate.split("-")
	intime=input("Time: ")
	intime=intime.split(":")
	inrange=input("Range: ")
	logcheck={}
	c=0
	with open("/var/log/syslog"),open("/var/log/auth.log"),open("/var/log/kern.log") as f:
		for line in f:
			if 
			logcheck[c]=thedate(line)
			c+=1
	return 0

if __name__=='__main__':
	main()
