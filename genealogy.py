#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from db import dbase 
from readData import readData

def depths(idx):
	pass

if __name__ == "__main__":
	#print readData(131339)
	print readData(131343)
	"""
	dbase.startDatabase()
	print dbase.writePhD(131343, u"Ferdinand Börner")
	print dbase.phdExists(131343)
	dbase.stopDatabase()"""
