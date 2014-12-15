#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Motor:
	def __init__(self,
			rpm=100, #Revolutions Per Minute
			hp=100, #Horsepower
			temp=10, #Temperature
			manufacturer="Volvo", #Manufacturer
			state="stop"): #Engine on/off
		self.rpm=rpm
		self.hp=hp
		self.temp=temp
		self.manufacturer=manufacturer
		self.state=state

	#Changes the state of the engine to be on or off
	def changestate(self, changestate):
		#If the value sent with the method is start or stop
		if changestate.lower() == "start" or changestate.lower() == "stop":
			#Set it to be start or stop.
			self.state=changestate
		#Fail check.
		else:
			print "Invalid state!"
			print "Changestate to start/stop!"

	#Do some fun driving test thingy
	def accelerate(self):
		#If the engine state is start
		if self.state.lower()=="start":
			#Set rpm to 100
			print "Engine has accelerated."
			self.rpm=100
		#If engine state is stop, tell the user that.
		elif self.state.lower()=="stop":
			print "The engine is off."
		#Fail check
		else:
			print "Engine state is abnormal!"
			print "Changestate to start/stop!"
#Inherits parent Motor
class Elmotor(Motor):
	def __init__(self,
			rpm=100,
			hp=100,
			temp=0,
			manufacturer="Volvo",
			state="stop",
			amp=1, #Ampere
			volt=10, #Volt
			eta=10, #Thermal efficiency
			charge=100): #Charge in battery
		#Initiate parent inhertiance
		Motor.__init__(self,rpm,hp,temp,manufacturer,state)
		self.amp=amp
		self.volt=volt
		self.eta=eta
		self.charge=charge
	#Recharge method to recharge battery
	def recharge(self, amount):
		#Fancily shows battery charge
		print "Current Charge [",
		for cl in range(0,(self.charge/10)):
			print "|",
		print "]"
		#Sets charge with the added value
		self.charge+=amount
		#EXPLOSIONS, if the battery is overcharged
		if self.charge > 100:
			print "Too much charge was inserted!"
			print "OH GOD! THE ENGINE EXPLODED!"
		#Otherwise, no explosions.. Just output again for new charge.
		elif self.charge <= 100:
			print "Battery charged [",
			for cl in range(0,(self.charge/10)):
				print "|",
			print "]"	
#Inherits Motor
class Bensinmotor(Motor):
	def __init__(self,
			rpm=100,
			hp=100,
			temp=0,
			manufacturer="Volvo",
			state="stop",
			cylinder=4, #Cylinders
			spark=10, #Spark Plug
			lpm=0.1, #Liters per Minute
			fuel=70): #Fuel in liters
		Motor.__init__(self,rpm,hp,temp,manufacturer,state)
		self.cylinder=cylinder
		self.spark=spark
		self.lpm=lpm
		self.fuel=fuel
	#Method for a driving test
	def driving(self, time, length):
		#If the engine state is on
		if self.state=="start":
			#Set meters per minute, disguised as per hour...
			mph=length/time
			#Sets rpm in relation to mph
			self.rpm=mph*25
			#sets fuel according to the loss in relation to driving time
			self.fuel=self.fuel-(time*self.lpm)
			#See if the fuel ran out or not
			if self.fuel < 0:
				print "FAILURE: You ran out of fuel!"
			else:
				print "SUCCESS: You got to your destination!"
			#Show results.
			print ("You ended with %d liters left in your tank" %self.fuel)
			print ("Your speed was %d rpm and %d mph" %(self.rpm, mph))
		#If the engine was off or otherwise malfunctioning
		elif self.state=="stop":
			print "The engine is off..."
		else:
			print "Engine failure!"



class Hybridmotor(Elmotor,Bensinmotor):
	def __init__(self,
			rpm=100,
			hp=100,
			temp=0,
			manufacturer="Volvo",
			state="stop",
			amp=1, #Ampere
			volt=10, #Volt
			eta=10, #Thermal efficiency
			charge=100, #Charge in battery
			cylinder=4, #Cylinders
			spark=10, #Spark Plug
			lpm=0.1, #Liters per Minute
			fuel=70): #Fuel in liters
		#Initiate parent inhertiance
		Elmotor.__init__(self,rpm,hp,temp,manufacturer,state,amp,volt,eta,charge)
		Bensinmotor.__init__(self,rpm,hp,temp,manufacturer,state,cylinder,spark,lpm,fuel)
		
