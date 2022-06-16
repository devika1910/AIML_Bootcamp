import sqlite3
conn = sqlite3.connect("Bootcamp.db")
conn.execute("drop table participants")
conn.close()