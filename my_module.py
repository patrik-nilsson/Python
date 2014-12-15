#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
 
currmonth = int(time.strftime("%m"))
currday = int(time.strftime("%d"))
curryear = int(time.strftime("%y"))
def bornyear (month, day, year):
	global currmonth
	global currday
	global curryear
	m=currmonth-month
	d=currday-day-1
	y=2000+curryear-year
	if m < 0:
		y=y-1
	elif m == 0:
		if d < 0:
			y=y-1
	return y
