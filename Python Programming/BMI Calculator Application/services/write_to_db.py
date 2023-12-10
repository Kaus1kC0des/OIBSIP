def write_bmi_to_db(userid, bmi, conn):
    c = conn.cursor()

    try:
        # Check if a record for the user already exists
        c.execute("SELECT * FROM bmi WHERE userid = ?", (userid,))
        record = c.fetchone()

        if record:
            # If a record exists, update it
            c.execute("UPDATE bmi SET bmi = ? WHERE userid = ?", (bmi, userid))
        else:
            # If no record exists, insert a new one
            c.execute("INSERT INTO bmi (userid, bmi) VALUES (?, ?)", (userid, bmi))

        conn.commit()
    except Exception as e:
        print(f"An error occurred: {e}")