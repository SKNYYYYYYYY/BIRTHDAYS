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

# create db and table
def setup_database(cur):
	cur.execute("CREATE DATABASE  IF NOT EXISTS birthdays")
	sql = """CREATE TABLE IF NOT EXISTS celeb  ( 
				no INT AUTO_INCREMENT PRIMARY KEY,
				month VARCHAR(10),
				generation VARCHAR(15),
				date VARCHAR(5),
				name VARCHAR(40),
				metadata VARCHAR(30),
				refcode INT(6)
		)"""	
	cur.execute(sql)
	sql = """CREATE TABLE IF NOT EXISTS authenticate (
				username VARCHAR(10),
				email VARCHAR(40),
				password VARCHAR(20),
				refcode VARCHAR(100) PRIMARY KEY
		)"""
	cur.execute(sql)
#save credentials
def save_credentials(cur, data):
	sql = 'INSERT INTO authenticate (username, email, password, refcode) VALUES(%s, %s, %s, %s)'
	cur.execute(sql, (data.username, data.email, data.password, data.refcode))
	return f"{data.username}'s credentials succesfully saved"

# validate  refcode
def validate_refcode(cur, refcode):
	cur.execute('SELECT COUNT(*) FROM authenticate WHERE refcode=%s', refcode)
	result = cur.fetchone()
	if 1 in result:
		return "code available"
	else:
		return "code not available"

# return the month celebrants
def get_month_celebrants(month, cur):
	cur.execute('SELECT * FROM whole_year WHERE month=%s', month)
	result = cur.fetchall()
	return result

# save new celebrant to the db
def save_celebrant(data, cur):
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