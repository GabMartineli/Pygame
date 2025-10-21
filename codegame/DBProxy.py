

import sqlite3


class DBProxy:

    def __init__(self, db_name):
        self.db_name = db_name
        self.connect = sqlite3.connect(db_name)
        self.connect.execute(
                            '''
                                CREATE TABLE IF NOT EXISTS dados(
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                name TEXT NOT NULL,
                                score INTEGER NOT NULL,
                                date TEXT NOT NULL)
                            '''
                            )
    
    def save(self, score_dict: dict):
        self.connect.execute('INSERT INTO dados (name, score, date) VALUES (:name, :score, :date)', score_dict)
        self.connect.commit()

    def retrieve_top10(self):
        return self.connect.execute('SELECT * FROM dados ORDER BY score DESC LIMIT 10').fetchall()

    def close(self):
        return self.connect.close()