#!/usr/bin/env python

import urllib2
from db import dbHandler

def depths(idx):
	pass

if __name__ == "__main__":
	handler = dbHandler()
	handler.startDatabase()

	handler.stopDatabase()
