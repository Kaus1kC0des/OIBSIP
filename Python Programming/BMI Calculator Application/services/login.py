import sqlite3

def login_user(userid, password, conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM login WHERE userid = ? AND password = ?", (userid, password))
    record = cur.fetchone()

    if record:
        return True
    else:
        return False