import pymysql


# create a mysql db connection
def mydb():
	return pymysql.connect(
		host='localhost',
		user='newton',
		password='safcoM',
		db='birthdays',
		autocommit=True
	)

# return the month celebrants
def get_month_celebrants(month, cur):
	cur.execute('SELECT * FROM whole_year WHERE month=%s', month)
	result = cur.fetchall()
	return result

# save new celebrant to the db
def save(data, cur):
	sql = 'INSERT INTO whole_year (month, generation, date, name, metadata) VALUES (%s, %s, %s, %s, %s)'
	cur.execute(sql, (data.month, data.generation, data.date, data.name, data.metadata))
	return f"{data.name} succesfully added"

#search celebrant
def search(name, cur):
	sql = "SELECT * FROM whole_year WHERE LOWER(name) LIKE %s"
	cur.execute(sql, (f"%{name.lower()}%",))
	result = cur.fetchall()
	if len(result) == 0:
		return f"Oops! '{name}' wasn't found. Double-check the spelling and try again."
	else:
		return result

#delete celebrant
def delete(name, cur):
	#check if name exist
	name_data = search(name, cur)
	if isinstance(name_data, tuple):		
		sql = "DELETE FROM whole_year WHERE name=%s"
		cur.execute(sql, name)
		return f"{name} deleted"
	else:
		return f"{name} does not exist"