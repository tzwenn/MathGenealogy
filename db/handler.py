# -*- coding: UTF-8 -*-

# Copyright (C) 2010 Sven Köhler  <tzwenn@users.berlios.de>

import os
import sqlite3

import sys

def errPrint(s):
	sys.stderr.write(str(s))

class dbHandler(object):
    """ Basic Database access and creating of table structure """ 
    
    def __init__(self):
        self.con = sqlite3.Connection
        self.cur = sqlite3.Cursor
        self.running = False
        self.filename = ""
    
    def connect(self):
        self.con = sqlite3.connect(self.filename)
        self.con.isolation_level = None
        self.cur = self.con.cursor()
        self.running = True
    
    def startDatabase(self, check_version = True):
        self.filename = "genealogy.db"
        exists = os.path.exists(self.filename)
        self.connect()
        if not exists:
            self.buildDataBaseStructure()
        elif check_version:
            self.checkVersion()
        
    def checkVersion(self):
        pass
        
    def execute(self, *args):
        try:
            self.cur.execute(*args)
            return True
        except (StandardError), e:
            errPrint(e)
            return False
    
    def executescript(self, *args):
        try:
            self.cur.executescript(*args)
            return True
        except (StandardError), e:
            errPrint(e)
            return False
    
    def iterdump(self):
        return self.con.iterdump()
    
    def fetchall(self, *args):
        try:
            self.cur.execute(*args)
            res = self.cur.fetchall()
            return res 
        except (StandardError), e:
            errPrint(e)
            return []
    
    def exec_fetchone(self, *args):
        try:
            self.cur.execute(*args)
            return self.cur.fetchone() 
        except (StandardError), e:
            errPrint(e)
            return None
    
    def fetchone(self):
        return self.cur.fetchone()
    
    def __iter__(self):
        return self    
    
    def next(self):
        return self.cur.next()
    
    def buildDataBaseStructure(self):
        self.executescript("""
            CREATE TABLE phd (
              id INTEGER PRIMARY KEY,
              name TEXT
            );
	    CREATE INDEX IDX_phd_id ON phd (id);

            CREATE TABLE thesis (
              id INTEGER PRIMARY KEY,
	      degree TEXT,
              year TEXT,
              title TEXT,
              school TEXT
            );
            CREATE INDEX IDX_thesis_id ON thesis (id);

            CREATE TABLE degree (
              studentID INTEGER,
              advisorID INTEGER,
              thesisID INTEGER
            );
            CREATE INDEX IDX_degree_sid ON degree (studentID);
            CREATE INDEX IDX_degree_aid ON degree (advisorID);
            CREATE INDEX IDX_degree_tid ON degree (thesisID);
        """)
    
    def readFromDump(self, dump):
        self.stopDatabase()
        os.remove(self.filename)
        self.connect()
        self.executescript(dump)
        self.restartDatabase()
    
    def stopDatabase(self):
        if self.running:
            self.con.commit()
            self.cur.close()
            self.con.close()
            self.running = False
            
    def restartDatabase(self, check_version = True):
        self.stopDatabase()
        self.startDatabase(check_version)

