import sqlite3

class HighScoreTable:
	
	def __init__(self):
		Scores = sqlite3.connect("Landerscores.db")
		cursor = connection.cursor()
		cursor.execute("CREATE TABLE hiscore (score, int)")
		cursor.execute("ALTER TABLE hiscore (name, str)")
		
	def addscore(self, name, points):
		try:
			cursor.execute("UPDATE hiscore SET score = points WHERE 'name' = true")
		except Exception as err:
			cursor.execute("INSERT INTO hiscore (name, score) VALUES (name, points)")
		
	def showscore(self):
		cursor.execute("SELECT * FROM hiscore ORDER BY score DESC")
