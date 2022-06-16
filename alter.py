import sqlite3
conn=sqlite3.connect('Bootcamp.db') #step 2 and step 3

'''
query--> alter table table_name add column column_name datatype constraints
'''
query = '''
        alter table participants add column study text not null
        '''
conn.execute(query)

conn.commit()
conn.close()