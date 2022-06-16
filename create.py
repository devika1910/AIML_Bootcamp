import sqlite3
conn=sqlite3.connect('Bootcamp.db') #step 2 and step 3

'''
query -> create table table_name(column_names datatype constraints(primary key, not null, unique),.......)
'''
query = '''
        create table participants(g_id int primary key,name text not null,branch text not null)
        '''
conn.execute(query)