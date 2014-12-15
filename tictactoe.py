#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
	game=[["#","#","#"],
	      ["#","#","#"],
	      ["#","#","#"]]
	A=1
	B=2
	C=3
	turn="X"
	continuous=0
	while continuous < 9:
		c=0
		print " A B C"
		for row in game:
			c+=1
			print str(c)+'|'.join(row)
		print "It's "+turn+"'s turn."
		print "Select a coordinate Ex. A,2"
		a2, a1=input(">"); a2=a2-1; a1=a1-1
		if game[a1][a2] == "X" or game[a1][a2] == "O":
			print "Position is already taken!"
			continue
		else:
			continuous+=1
			game[a1][a2]=turn
		isit=gameover(game,turn)
		if isit == "break":
                	c=0
	                for row in game:
        	                c+=1
                	        print str(c)+'|'.join(row)
			print turn+" got three in a row!"
			break
		if turn=="X":
			turn="O"
		else:
			turn="X"
		if continuous == 9:
			print "It's a draw!"
			break
	return 0

def gameover(game,Var):
	if game [0][0] == Var and game[0][0] == game[1][0] and game[1][0] == game[2][0]:
		return "break"
	elif game [0][1] == Var and game[0][1] == game[1][1] and game[1][1] == game[2][1]:
		return "break"
	elif game [0][2] == Var and game[0][2] == game[1][2] and game[1][2] == game[2][2]:
		return "break"
	elif game [0][0] == Var and game[0][0] == game[0][1] and game[0][1] == game[0][2]:
		return "break"
	elif game [1][0] == Var and game[1][0] == game[1][1] and game[1][1] == game[1][2]:
		return "break"
	elif game [2][0] == Var and game[2][0] == game[2][1] and game[2][1] == game[2][2]:
		return "break"
	elif game [0][0] == Var and game[0][0] == game[1][1] and game[1][1] == game[2][2]:
		return "break"
	elif game [0][2] == Var and game[0][2] == game[1][1] and game[1][1] == game[2][0]:
		return "break"
	else:
		return 0
		

if __name__=='__main__':
	main()
