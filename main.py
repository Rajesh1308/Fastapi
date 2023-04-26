from fastapi import FastAPI, Path
import uvicorn
import os
import subprocess

app = FastAPI()

@app.get("/")
def home():
    a = 5
    return {"Result" : "The site is up and running"}


@app.get("/leap-year")
def get_item(year: int):
    if year%4 == 0:
        res = "It is a leap year"
    else:
        res = "It is not a leap year"
    return res

@app.get("/path-param")
def path_param(value):
    res = os.system(value)
    returned_text = subprocess.check_output(value, shell=True, universal_newlines=True)
    return {"The value you entered in path is " : returned_text}

if '__main__' == __name__:
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)