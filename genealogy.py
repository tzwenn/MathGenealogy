#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from db import dbase 
from search import depthSearch
from optparse import OptionParser

def optsearch(option, opt, value, parser):
	dbase.startDatabase()
	depthSearch(value)
	dbase.stopDatabase()

def optdisplay(option, opt, value, parser):
	dbase.startDatabase()
	print "display mal"
	dbase.stopDatabase()

if __name__ == "__main__":
	parser = OptionParser("%prog [Operation] [Arguments]", version="%prog 0.1")
	parser.add_option("-s", "--search", type="int", dest="id", help="search genealogy of Ph. D. with ID", action="callback", callback=optsearch)
	parser.add_option("-d", "--display", type="int", dest="id", help="display genealogy of Ph. D. with ID", action="callback", callback=optdisplay)
	(options, args) = parser.parse_args()

