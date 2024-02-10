import psycopg2
import random

conn = None
cur = None

try:
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="postgres",
        user="postgres",
        password="openthedoor"
        )

    cur = conn.cursor()         

    cur.execute('DROP TABLE IF EXISTS Demopull')
    create_table = """CREATE TABLE IF NOT EXISTS Demopull(
        Rollno int PRIMARY KEY,
        Name varchar,
        Test1 int,
        Test2 int
        )"""
    cur.execute(create_table)
    print("[+] Table Demopull Created Successfully")
        
    conn.commit()

except Exception as error:
    print(error)

finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()