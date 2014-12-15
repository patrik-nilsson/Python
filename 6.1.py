#!/usr/bin/env python
# -*- coding: utf-8 -*-
from motor import Motor
def main():
	Volvomotor=Motor(0,100,0,"Volvo","Stop")
	state=raw_input("Motor state: ")
	Volvomotor.changestate(state)
	Volvomotor.accelerate()
	print "Current speed: "+str(Volvomotor.rpm)+"rpm"
	return 0

if __name__=='__main__':
	main()
