import sqlite3
with sqlite3.connect(":memory:") as database:
    database.execute("CREATE TABLE users (name TEXT)")
    database.execute("INSERT INTO users VALUES (?)", ("Mira",))
    value = "Mira' OR '1'='1"
    rows = database.execute("SELECT name FROM users WHERE name = ?", (value,)).fetchall()
    print(rows)
database.close()
