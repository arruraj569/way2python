import sqlite3
with sqlite3.connect(":memory:") as database:
    database.execute("CREATE TABLE results (name TEXT, passed INTEGER)")
    database.execute("INSERT INTO results VALUES (?, ?)", ("login", 1))
    rows = database.execute("SELECT name FROM results WHERE passed = ?", (1,)).fetchall()
    print(rows)
database.close()
