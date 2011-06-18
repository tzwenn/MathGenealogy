# -*- coding: UTF-8 -*-

import urllib2
import re

#urlname = lambda idx: "http://genealogy.math.ndsu.nodak.edu/id.php?id=%d" % idx
urlname = lambda idx: "http://www.genealogy.ams.org/id.php?id=%d" % idx

html_escaped = {
	"&Auml;": u'Ä',
	"&Ouml;": u'Ö',
	"&Uuml;": u'Ü',
	"&auml;": u'ä',
	"&ouml;": u'ö',
	"&uuml;": u'ü',
	"&szlig;": u'ß',
	"&Agrave;": u'À',
	"&Egrave;": u'È',
	"&Ograve;": u'Ò',
	"&Ugrave;": u'Ù',
	"&agrave;": u'à',
	"&egrave;": u'è',
	"&ograve;": u'ò',
	"&ugrave;": u'ù',
	"&Aacute;": u'Á',
	"&Eacute;": u'É',
	"&Oacute;": u'Ó',
	"&Uacute;": u'Ú',
	"&aacute;": u'á',
	"&eacute;": u'é',
	"&oacute;": u'ó',
	"&uacute;": u'ú',
	"&amp;": u'&',
	"&AElig;": u'Æ',
	"&aelig;": u'æ',
	"&#324;": u'ń',
}


def unescape(s):
	for old, new in html_escaped.iteritems():
		s = s.replace(old, new)
	return re.sub("\s+", " ", s)

def tagpart(text, delim):
	a, dummy, b = text.partition(delim)
	return a.strip(), b

def fetchPage(idx):
	f = urllib2.urlopen(urlname(idx))
	if not f:
		return ""
	text = f.read().decode('utf-8')
	f.close()
	return unescape(text)

def readPhD(idx, text):
	return (idx, re.search("<h2.*?>(.*?)</h2>", text).group(1).strip())

def readThesis(idx, text):
	text = text.partition("<span style=\"margin-right: 0.5em\">")[2]
	degree, text = tagpart(text, "<span style=\"color: #006633; margin-left: 0.5em\">")
	school, text = tagpart(text, "</span>")
	year, text = tagpart(text, "</span>")
	title, text = tagpart(text.partition("<span style=\"font-style:italic\" id=\"thesisTitle\">")[2], "</span>")
	return (degree, year, title, school)

def readDegree(idx, text):
	mo = re.search('<p style="text-align: center; line-height: 2.75ex">(.*?)</p>', text)
	if mo is None:
		return []
	text = mo.group(1)
	return [(idx, int(aID)) for aID in re.findall(r'<a.*?id=(.*?)">', text)]

def readData(idx):
	text = fetchPage(idx)
	return readPhD(idx, text), readThesis(idx, text), readDegree(idx, text)

