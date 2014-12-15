#!/usr/bin/env python
# -*- coding: utf-8 -*-
from motor import Hybridmotor
def main():

	#Create Hybrid Engine
	Motor1=Hybridmotor()
	#Start/stop the Engine for Motor1
	reply=raw_input("Start/Stop engine: ")
	Motor1.changestate(reply)
	#Run Fuel driving test with the Hybrid Engine?
	reply=raw_input("Run test? (y/n) ")
	if reply.lower() == "y":
		#Test Motor1 with set values for time and length
		print "Motor1 starts driving..."
		Motor1.driving(60,9000)
	else:
		#If you didn't say you wanted to do the test
		print "Assuming you meant no..."
	#Input for how long, and how far, you wanna drive
	time=input("For how long do you intend to drive? (In minutes): ")
	length=input("How far do you intend to drive? (In meters): ")
	Motor1.driving(time,length)

	#Stuff to charge the Hybrid Engine
	Motor1.charge=46
	energy=str(Motor1.charge)
	reply=input("Current charge at "+energy+"% Insert how much charge? ")
	Motor1.recharge(reply)
	
	return 0

if __name__=='__main__':
	main()
