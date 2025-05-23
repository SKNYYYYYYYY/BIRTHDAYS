import uvicorn
from fastapi import FastAPI, Form
# from database import setup_database, get_month_celebrants,\
# save, search, mydb, delete, validate_refcode
from database import *
from pydantic import BaseModel
import logging


app = FastAPI()

# create database connection
conn = mydb()
cur = conn.cursor()

# set up logging
# logger = logging.getname(__name__)

#initial startup
@app.on_event("startup")
def create_db_and_table():
	try:
		setup_database(cur)
		print("birthdays database and whole_year table created succesfully ")
	except Exception as e:
		print(f"Error creating birthdays database and whole_year table. \n{e}") 
		return

#root endpoint
@app.get("/")
def root():
	return {"message": "WELCOME"}

class Credentials(BaseModel):
	username: str
	email: str
	password: str
	refcode: str

@app.post("/admin_signup")
def signup(data: Credentials):
	try:
		return save_credentials(cur, data)
	except Exception as e:
		print(e)

# validate refcode
@app.get("/referral_code")
def referral(refcode: str):
	return validate_refcode(cur, refcode)

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
	return save_celebrant(data,cur)

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
