from db import dbase
import sys

visitedPhDs = set([])

def formatNode(name):
	return '[label = "%s" shape="plaintext"]' % name

def visPhD(idx, depth=1000):
	if idx in visitedPhDs:
		return ""
	phd = dbase.readPhD(idx)
	if phd is None:
		print sys.stderr >> "[Display] Failed reading", idx
		return ""
	advisors = dbase.getAdvisors(idx)
	res = ""
	visitedPhDs.add(idx)
	if depth > 0:
		for aID in advisors:
			try:
				res += "%s\n" % visPhD(aID, depth - 1)
			except Exception, e:
				print sys.stderr >> "[Display] Exception occured processing %d:" % aID, e
		res += "\n".join(["  %d -> %d" % (idx, aID) for aID in advisors])
	return res+"\n  %d %s" % (idx, formatNode(phd[1]))

def graphVIZ(idx):
	visitedPhDs = set([])
	return ("digraph Genealogy {\n%s\n}" % visPhD(idx)).encode("utf-8")

if __name__ == "__main__":
	dbase.startDatabase()
	print "digraph Genealogy {"
	print visPhD(131343).encode("utf-8")
	print visPhD(29774).encode("utf-8")
	print visPhD(153847).encode("utf-8")
	print "}"
	dbase.startDatabase()

