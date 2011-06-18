#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
from db import dbase 
from readData import readData

def depths(idx, depth=1000):
	if dbase.phdExists(idx) or depth < 0:
		return
	phd, (degree, year, title, school), degrees = readData(idx)
	if dbase.writePhD(idx, phd[1]) is None:
		return
	tidx = dbase.writeThesis(degree, year, title, school)
	if tidx is None:
		return
	for sID, aID in degrees:
		if not dbase.writeDegree(sID, aID, tidx):
			return
	for dummy, aID in degrees:
		try:
			depths(aID, depth-1)
		except Exception:
			pass

if __name__ == "__main__":
	if len(sys.argv) > 1:
		dbase.startDatabase()
		for idx in map(int, sys.argv[1:]):
			depths(idx)
		dbase.stopDatabase()
	else:
		print "Gib mir mal eine StartID"
