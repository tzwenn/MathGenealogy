from db import dbase
from readData import readData
import sys

def depthSearch(idx, depth=1000):
	if dbase.phdExists(idx):
		return
	if depth < 0:
		print >> sys.stderr, "[Search] Exceeded search depth on", idx
	phd, (degree, year, title, school), degrees = readData(idx)
	if dbase.writePhD(idx, phd[1]) is None:
		print >> sys.stderr, "[Search] Failed on writing Ph. D.", idx
		return 
	tidx = dbase.writeThesis(degree, year, title, school)
	if tidx is None:
		print >> sys.stderr, "[Search] Failed on writing thesis", tidx
		return
	for sID, aID in degrees:
		if not dbase.writeDegree(sID, aID, tidx):
			print >> sys.stderr, "[Search] Failed on writing degrees (%d, %d)" % (sID, aID) 
			return 
	for dummy, aID in degrees:
		try:
			depthSearch(aID, depth-1)
		except Exception, e:
			print >> sys.stderr, "[Search] Exception occured processing %d:" % aID, e

