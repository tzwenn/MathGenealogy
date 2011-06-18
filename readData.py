# -*- coding: UTF-8 -*-

import urllib2
import re
#import htmllib

urlname = lambda idx: "http://genealogy.math.ndsu.nodak.edu/id.php?id=%d" % idx

def unescape(s):
	return re.sub("\s+", " ", s)
	"""p = htmllib.HTMLParser(None)
	p.save_bgn()
	p.feed(s)
	return p.save_end()"""

def fetchPage(idx):
	f = urllib2.urlopen(urlname(idx))
	if not f:
		return ""
	text = f.read().decode('utf-8')
	f.close()
	return unescape(text)

def readPhD(idx, text):
	tmp = text.partition("<h2 style=\"text-align: center; margin-bottom: 0.5ex; margin-top: 1ex\">")[2]
	name = tmp.partition("</h2>")[0].strip()
	return (idx, name)

def readDegree(idx, text):
	text = text.partition("<span style=\"margin-right: 0.5em\">")[2]
	degree, dummy, text = text.partition("<span style=\"color: #006633; margin-left: 0.5em\">")
	school, dummy, text = text.partition("</span>")
	year = text.partition("</span>")[0].strip()
	degree = degree.strip()
	school = school.strip()
	print (degree, year, school)

def readData(idx):
	text = fetchPage(idx)
	return readPhD(idx, text), readDegree(idx, text)
