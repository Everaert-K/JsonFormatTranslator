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

# create_table()
# j = '''{"address" : "https://www.google.com ","content" : {"seasons" : [{"text": "winter"},{"text": "spring"},{"text": "summer"},{"text": "autumn"}],"description" : "All seasons"},"updated" : "2021-02-26T08:21:20+00:00","author" : {"username" : "Bob","id" : "68712648721648271"},"id" : "543435435","created" : "2021-02-25T16:25:21+00:00","counters" : {"A" : 3,"B" : 0},"type" : "main"}'''
# o = OldFormat(j)
# n = TranslatorOldToNew.translate(o) 
# insert(n)     
# conn.close()
