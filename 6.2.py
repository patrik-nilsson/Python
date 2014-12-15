#!/usr/bin/env python
# -*- coding: utf-8 -*-
from motor import Elmotor,Bensinmotor
import cPickle as pickle
def main():

	#Create Electric Engine
	Motor3=Elmotor()
	#Create Fuel Engine
	Motor1=Bensinmotor()
	#Start/stop the Engine for Motor1
	reply=raw_input("Start/Stop engine: ")
	Motor1.changestate(reply)
	#Run Fuel Engine driving test?
	reply=raw_input("Run test? (y/n) ")
	if reply.lower() == "y":
		#Create additional Fuel Engine and set fuel to 1 liter
		Motor2=Bensinmotor()
		Motor2.fuel=1
		#Test Motor1 with set values for time and length
		print "Motor1 starts driving..."
		Motor1.driving(60,9000)
		#Same with Motor2, but Motor2 is off, so it'll "fail".
		print "Motor2 starts driving..."
		Motor2.driving(20,1000)
	else:
		#If you didn't say you wanted to do the test
		print "Assuming you meant no..."
	#Input for how long, and how far, you wanna drive
	time=input("For how long do you intend to drive? (In minutes): ")
	length=input("How far do you intend to drive? (In meters): ")
	Motor1.driving(time,length)

	#Stuff to charge the Electric Engine
	Motor3.charge=46
	energy=str(Motor3.charge)
	reply=input("Current charge at "+energy+"% Insert how much charge? ")
	Motor3.recharge(reply)
	
	#Save the values we got.
	f=open("6-2.data", "w")
	pickle.dump(Motor1, f)
	pickle.dump(Motor2, f)
	pickle.dump(Motor3, f)
	return 0

if __name__=='__main__':
	main()
