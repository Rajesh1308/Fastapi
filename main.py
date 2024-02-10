from fastapi import FastAPI, Path
import uvicorn
import psycopg2
import os
import subprocess

conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="postgres",
    user="postgres",
    password="openthedoor"
)

cur = conn.cursor()

app = FastAPI()

@app.get("/")
def home():
    
    
    return {"Result" : "The site is up and running" }


@app.get("/leap-year")
def get_item(year: int):
    if year%4 == 0:
        res = "It is a leap year"
    else:
        res = "It is not a leap year"
    return res

@app.get("/path-param")
def path_param(value):
    #res = os.system(value)
    #returned_text = subprocess.check_output(value, shell=True, universal_newlines=True)
    #return {"The value you entered in path is " : returned_text}
    return "Stopped due to identification of a bug"

@app.get("/add_marks")
async def add_marks(rollno: str, Name: str, Test1: int, Test2: int):
    try:
        add_command = "INSERT INTO Demopull (Rollno, Name, Test1, Test2) VALUES (%s, %s, %s, %s)"
        add_value = (rollno, Name, Test1, Test2)
        cur.execute(add_command, add_value)
        return "Record added successfully"
    except:
        conn.rollback()
        
    conn.commit()
    return "Record not added"
    

if '__main__' == __name__:
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)