from fastapi import FastAPI, Path
app = FastAPI()

inventory = { 
    1 : {
    "Name" : "tea Powder",
    "Price ": 96.00,
    "Quantity" : 1000
    },
    2 : {
    "Name" : "Coffee",
    "Price": 102.00,
    "Quantity" : 2065
    }
}

@app.get("/")
def home():
    a = 5
    return {"Data" : "Testing", "value" : a}

@app.get("/about")
def about():
    return {"Name" : "Rajesh A"}

@app.get("/get_item/{item_id}")
def get_item(item_id: int = Path(description="The ID of the item you wish",gt=0,lt=3)):
    return inventory[item_id]

@app.get("/leap/{year}")
def leap(year: int):
    if (year%4 == 0):
        ans = "It is a leap year"
    else:
        ans = "It is not a leap year"
    return ans

@app.get("/get-by-name")
def get_item(Name: str):
    for item_id in inventory:
        if inventory[item_id]["Name"] == Name:
            return inventory[item_id]
    return {"Data " : "Not found"}
