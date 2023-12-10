import sqlite3
import uuid

def generate_userid():
    return str(uuid.uuid4())[:8]

def create_user(name, age, email, conn):
    cur = conn.cursor()
    userid = generate_userid()  # Generate a unique userid

    while True:
        try:
            cur.execute("INSERT INTO user(name, age, email, userid) VALUES(?, ?, ?, ?)",
                        (name, age, email, userid))
            conn.commit()
            return userid  # Return the userid
        except sqlite3.IntegrityError:
            # If a collision occurs, generate a new userid and try again
            userid = generate_userid()
            continue
        except Exception as e:
            return str(e)