import psycopg2
import random

conn = None
cur = None

conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="postgres",
    user="postgres",
    password="openthedoor"
    )

cur = conn.cursor()

cur.execute("SELECT * FROM Demopull")
records = cur.fetchall()
for record in records:
    print(record)
conn.commit()
conn.close()