import sqlite3
con = sqlite3.connect('bootcamp.db')
str = con.execute("pragma table_info('attendances')")
print(str)
for i in str:
    print(i)
