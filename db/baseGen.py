# -*- coding: UTF-8 -*-

from handler import dbHandler

class dbBaseGen(dbHandler):

	def writePhD(self, idx, name):
		if not self.execute("""INSERT INTO phd
			(id, name) VALUES (?, ?)""",(idx, name)):
			return None
		self.con.commit() # Nötig?
		return idx

	def writeThesis(self, degree, year, title, school):
		if not self.execute("""INSERT INTO thesis
			(degree, year, title, school) VALUES (?, ?, ?, ?)""",
			(degree, year, title, school)):
			return None
		self.con.commit()
		return self.cur.lastrowid

	def writeDegree(self, student, advisor, thesis):
		if not self.execute("""INSERT INTO degree
				(studentID, advisorID, thesisID)
				VALUES (?, ?, ?)""", (student, advisor, thesis)):
			return None
		return advisor


	def readPhD(self, idx):
		return self.exec_fetchone("SELECT * FROM phd WHERE id=:1", (idx,))

	def readThesis(self, idx):
		return self.exec_fetchone("SELECT * FROM thesis WHERE id=:1", (idx,))

	def getAdvisors(self, studentID):
		""" Returns advisors of a student
		    This is a multiset, not a normal set!
		"""
		return map(lambda tpl: tpl[0], self.fetchall("""SELECT advisorID FROM degree
			WHERE studentID=:1""", (studentID, )))

	def getStudents(self, advisorID):
		""" Returns students of an advisor
		    This is a multiset, not a normal set!
		"""
		return map(lambda tpl: tpl[0], self.fetchall("""SELECT studentsID FROM degree
			WHERE advisorID=:1""", (advisorID, )))

	def phdExists(self, idx):
		return self.readPhD(idx) is not None

