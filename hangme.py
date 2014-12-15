#!/usr/bin/env python
# -*- coding: utf-8 -*-

def hangme(fails):
	if fails == 1:
		print "_____"
	if fails == 2:
		print """  |  
_____"""
	if fails == 3:
		print """  |  
  |  
_____"""
	if fails == 4:
		print """  |  
  |
  |  
_____"""
	if fails == 5:
		print """  _______
  |   
  |
  |   
_____"""
	if fails == 6:
		print """  _______
  |   o
  |   
  |
_____"""
	if fails == 7:
		print """  _______
  |   o
  |   |
  |   
_____"""
	if fails == 8:
		print """  _______
  |   o
  |  /|  
  |
_____"""
	if fails == 9:
		print """  _______
  |   o
  |  /|\\
  |
_____"""
	if fails == 10:
		print """  _______
  |   o
  |  /|\\
  |  /
_____"""
	if fails == 11:
		print """  _______
  |   o
  |  /|\\
  |  / \\
_____"""
			
	return 0
