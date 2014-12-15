#!/usr/bin/env python
# -*- coding: utf-8 -*-
import operator
import random
import hangme

# THE GAME BEGINS IN MAIN, NOT IN START

def start(word,c,guesses,length,reply,fails,dic):
	#dict for drawing the characters of the correct word
	correct={}
	#Puts an underscore on every position in the dict
	for count in range(0,len(word),1):
		correct[count]="_"
	while True:
		#Check to see if the player has lost.
		if fails == 11:
			return "lose"
		#counter for putting letters in the drawing of the word and it's hidden letters
		c2=0
		#Draws the word with hidden letters
		for letters in word:
			#if the letter in the word is in the guessed letters, draw that letter
			if letters in guesses.values():
				correct[c2]=letters
				print correct[c2],
			#else, draw an underscore
			else:
				print correct[c2],
			#necessary counter to place the letter in the correct position
			c2+=1
		#adds a return since the above draw puts everything on one line
		print ""
		#Checks if there is even a single underscore in the correct-dict. If there isn't, you've won.
		if "_" not in correct.values():
			return "win"
		#Counter for guesses made increases
		c+=1
		#Loop to check so you don't make the same guess twice
		while True:
			#var to check if you did guess the same twice
			donotcontinue=0
			#get input into reply
			reply=raw_input("Gissa en bokstav: ")
			#cheat to check the current words in the dictionary and the word
			if reply == "show":
				print dic
				print word
				continue
			#Checks through guesses to see if the reply is in there
			for letter in guesses:	
				if reply == guesses[letter]:
					#If it is, do not continue
					donotcontinue=1
			#If the reply wasn't in guesses, break this loop
			if donotcontinue==0:
				break
			else:
				print ("Du har redan gissat på %s" %reply)
		#Put the reply into a guesses space
		guesses[c]=reply
		#Draw the guessed letters
		for letter in guesses:
			print guesses[letter],
		print ""
		#If you guessed a wrong letter, add to fails.
		if reply not in word:
			fails+=1
		#Draw the hangman
		hangme.hangme(fails)
			
def main():
	#Create var for the length of the word
	length=0
	#Makes sure you only put in a word length from 5 to 10
	while length < 5 or length > 10:
		length=input("Välj antal bokstäver (5-10) ")
	#failed guesses counter
	fails=0
	#result from the game var
	result=None
	#copy of the last chosen word
	saveword=None
	#dictionary of all words
	dic={}
	#copy of the last available dictionary
	savedic={}
	#Counter to fill up the dictionary
	c1=0
	#Counter to count the amount of rounds gone by for the guesses dict
	#Could probably be bundled with fails, but meh.
	c2=0
	#dictionary for the guessed letters
	guesses={}
	#dictionary for which keys to remove (explained later)
	remove={}
	#Put the file's words into a dictionary
	#Opens the file during the following tasks and put it's content in the variable f.
	with open("svenskaord.txt") as f:
		#Read each line from the file per loop.
		for line in f:
			#Split the lines into words
			for word in line.split():
				#If the word is as long as, the chosen length, put it in the dictionary
				if len(word) == length:
					dic[c1]=word
					#increase counter for position in dictionary
					c1+=1
	#Choose a random word from the dictionary
	theword=random.choice(dic.values())
	while True:
		if result=="win":
			print "Du vann!"
			return 0
		elif result=="lose" or fails==11:
			print "Du förlorade.."
			return 0
		for letters in theword:
			print "_",
		print ""
		#Counter for guesses made
		c2+=1
		#Loop to check so you don't make the same guess twice
		while True:
			donotcontinue=0
			reply=raw_input("Gissa en bokstav: ")
			if reply == "show":
				print dic
				print theword, saveword
				continue
			#Checks through guesses to see if the reply is in there
			for letter in guesses:	
				if reply == guesses[letter]:
					#If it is, do not continue
					donotcontinue=1
			#If the reply wasn't in guesses, break this loop
			if donotcontinue==0:
				break
			else:
				print ("Du har redan gissat på %s" %reply)
		#Put the reply into a guesses space
		guesses[c2]=reply

		#Check if letter is in any word.
		#Remove those words from the dictionary.
		#First; decide which keys in the dictionary to remove, and place those in remove.
		for word in dic:
			if reply in dic[word].lower():
				remove[word]=word
			
		#Then, remove those keys. Had to be done seperately, since it loops through
		#the dictionary, and it didn't like that it was edited while it was doing that.
		for word in remove:
			savedic[word]=dic[word]
			del dic[word]

		#If the word is removed, get a new word.
		if reply in theword:
			saveword=theword
			if dic:
				theword=random.choice(dic.values())
			else:
				result=start(saveword,c2,guesses,length,reply,fails,dic)
				dic={}
				continue
		#Reset remove to nothing.
		remove={}
		#Print guessed letters.
		for letter in guesses:
			print guesses[letter],
		print ""

		fails+=1
		hangme.hangme(fails)
	return 0

if __name__=='__main__':
	main()
