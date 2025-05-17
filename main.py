import uvicorn
from fastapi import FastAPI, Form
from database import get_month_celebrants,save, search, mydb, delete
from pydantic import BaseModel


app = FastAPI()

# create database connection
conn = mydb()
cur = conn.cursor()

#root endpoint
@app.get("/")
def root():
	return {"message": "WELCOME"}

#month endpoint
@app.get("/month")
async def month_celebrants(month):
	return get_month_celebrants(month, cur)

class Celebrant(BaseModel):
	month: str
	generation: str
	date: str
	name: str
	metadata: str

# new celebrant endpoint
@app.post("/new_celebrant")
async def new_celebrant(data: Celebrant):
	return save(data,cur)

# search celebrant endpoint
@app.get("/search")
async def search_celebrant(name):
	return search(name, cur)

# delete celebrant endpoint
@app.delete("/delete")
async def delete_celebrant(name):
	return delete(name, cur)


if __name__ == "__main__":
	uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
