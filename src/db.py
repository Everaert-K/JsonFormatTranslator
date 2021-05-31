from Format import NewFormat

import psycopg2

class database:
    def __init__(self):
        self.conn = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="root",
            password="root"
        )
        self.conn.autocommit = True
        # self.create_table()

    def __del__(self):
        self.conn.close()

    def create_table(self):
        s1 = 'DROP TABLE IF EXISTS jsonobjects'
        s2 = 'CREATE TABLE jsonobjects (id serial NOT NULL PRIMARY KEY,info json NOT NULL);'
        cursor = self.conn.cursor()
        cursor.execute(s1)
        cursor.execute(s2)

    def insert(self,newFormat):
        json_string = newFormat.getJson()
        s = '''INSERT INTO jsonobjects (info) VALUES(\''''+json_string+'''\');'''
        cursor = self.conn.cursor()
        cursor.execute(s)

    def close_connection(self):
        self.conn.close()

    def open_connection(self):
        self.conn = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="root",
            password="root"
        )
        self.conn.autocommit = True

    def retrieve_all(self):
        cursor = self.conn.cursor()
        query = '''select * from jsonobjects'''
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows
    
    def retrieve_object_with_id(self,id):
        cursor = self.conn.cursor()
        query = '''select info from jsonobjects where id='''+id
        cursor.execute(query)
        row = cursor.fetchone()
        return row

