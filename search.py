from db import dbase
from readData import readData

def depthSearch(idx, depth=1000):
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
			depthSearch(aID, depth-1)
		except Exception, e:
			print "Exception occured processing %d:" % aID, e

