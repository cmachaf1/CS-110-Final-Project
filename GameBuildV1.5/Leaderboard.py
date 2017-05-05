import sqlite3

class LeaderBoard:
    #create cursor object
    #connect to database
    #create alter capability for high score 
    def __init__(self, score):
        self.conn = sqlite3.connect("LeaderBoard.db")
        self.tablename = "leaderboard"
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute('CREATE TABLE self.tablename (name, str)') 
            self.cursor.execute("ALTER TABLE self.tablename ADD COLUMN (score, int)")
        except sqlite3.OperationalError as err:
            print(err)
    def InsertHighScore (self, name, score):
        self.cursor.fetchall()
        self.cursor.execute("INSERT INTO self.tablename VALUES(name, score)")
        self.cursor.execute("SELECT * FROM self.tablename order by score DESC;")

        #Close connection to db
    def closeConnection(self):
        self.conn.commit()
        self.cursor.close()

    

   
        
    
