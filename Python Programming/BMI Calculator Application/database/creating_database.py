import sqlite3 as sql

def create_database():
    with open("master.db"):
        conn = sql.connect('master.db')
        cur = conn.cursor()
        cur.execute("CREATE TABLE user (userid TEXT PRIMARY KEY, name TEXT NOT NULL, age INTEGER NOT NULL, email TEXT NOT NULL)")
        cur.execute("CREATE TABLE login ( userid TEXT PRIMARY KEY, password TEXT NOT NULL, FOREIGN KEY(userid) REFERENCES user(userid))")
        cur.execute("CREATE TABLE bmi (userid TEXT PRIMARY KEY, bmi REAL NOT NULL, prev_bmi REAL, date TEXT NOT NULL, FOREIGN KEY(userid) REFERENCES user(userid))")
        conn.commit()
        conn.close()

create_database()