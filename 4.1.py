#!/usr/bin/env python
# -*- coding: utf-8 -*-
import operator

def main():
	#Create dictionary
	dic={}
	#Make sure the file can be opened.
	try:
		#Opens the file during the following tasks and put it's content in the variable f.
		with open("aohf.txt") as f:
			#Read each line from the file per loop.
			for line in f:
				#Split the lines into words
				for word in line.split():
					#Remove any special characters
					a=word.lower().replace('"','').replace(',','').replace('.','').replace('!','').replace('?','').replace(':','').replace(';','')
					#If the word doesn't have a positions in the dictionary, add it.
					if a not in dic:
						dic[a]=1
					#Otherwise, +1 the value of it.
					else:
						dic[a]+=1

		#create the variable words and make it into a dictionary, use the sorted function
		#to sort the items in our dictionary in the order of the second operator (the value)
		#instead of by name of the key. Then reverse the soring, to put the highest at the top
		# and at last only get 100 of the values.
		words = dict(sorted(dic.iteritems(), key=operator.itemgetter(1), reverse=True)[:100])
		#Print out the entire dictionary "words" with their respective value next to them, in order.
		for key, value in sorted(words.iteritems(), key=operator.itemgetter(1), reverse=True):
			print str(key)+" "+str(value)
	except:
		#If any error occurred (the file wasn't found)
		print "File aohf.txt doesn't exist!"

	return 0

if __name__=='__main__':
	main()
