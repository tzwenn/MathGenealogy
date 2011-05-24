#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import urllib2
from db import dbase 

def depths(idx):
	pass

if __name__ == "__main__":
	dbase.startDatabase()
	print dbase.writePhD(131343, u"Ferdinand Börner")
	print dbase.readPhD(131343)
	dbase.stopDatabase()
