import sqlite3
con=sqlite3.connect('bootcamp.db')
con.execute("insert into attendances values(117,'BheemreddyDevika',100)")
con.execute("insert into attendances values(118,'sharanya',99)")
con.execute("insert into attendances values(127,'harini',97)")
con.execute("insert into attendances values(128,'akhila',98)")
con.execute("insert into attendances values(140,'pranay',98)")
con.commit()
con.close()