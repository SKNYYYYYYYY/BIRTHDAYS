
---

```markdown
# 🎉 Birthday Celebrants API

A simple FastAPI application to manage birthday celebrants using a MySQL database.

## 🚀 Features

- Add a new celebrant to the database
- Search for a celebrant by name
- View celebrants by month
- Delete a celebrant by name

## 🧰 Tech Stack

- FastAPI
- Uvicorn (ASGI server)
- PyMySQL (MySQL connector)
- MySQL

## 🔧 Setup Instructions

1. **Clone the repository**  
   ```bash
   git clone <repo_url>
   cd <project_folder>
````

2. **Set up MySQL**
   Ensure you have MySQL running and create a database named `birthdays` with the following table:

   ```sql
   CREATE TABLE whole_year (
       id INT AUTO_INCREMENT PRIMARY KEY,
       month VARCHAR(20),
       generation VARCHAR(20),
       date VARCHAR(10),
       name VARCHAR(100),
       metadata TEXT
   );
   ```

3. **Update database credentials** in `database.py`:

   ```python
   pymysql.connect(
       host='localhost',
       user='your_user',
       password='your_password',
       db='birthdays',
       autocommit=True
   )
   ```

4. **Install dependencies**

   ```bash
   pip install fastapi uvicorn pymysql
   ```

5. **Run the FastAPI server**

   ```bash
   python main.py
   ```

---

## 📫 API Endpoints

### ✅ Root

* **GET /**
  Returns a welcome message.

---

### 📅 Get Celebrants by Month

* **GET /month?month=June**
  Returns celebrants born in the specified month.

---

### 🆕 Add New Celebrant

* **POST /new\_celebrant**
  **Request Body (JSON):**

  ```json
  {
    "month": "June",
    "generation": "4th",
    "date": "21st",
    "name": "Kip",
    "metadata": "s/o Newton"
  }
  ```

---

### 🔍 Search Celebrant by Name

* **GET /search?name=kip**
  Returns celebrants matching the name (case-insensitive).

---

### ❌ Delete Celebrant

* **DELETE /delete?name=kip**
  Deletes the celebrant with the exact name match.

---

## ✅ Example JSON Response

```json
[
  [33, "April", "4th", "14th", "Ryan Kiplangat", "s/o Kenneth/Elizabeth"],
  [100, "November", "3rd", "12th", "Brian Kiplangat Bett", "s/o Evaline"]
]
```

---

## 📬 License

MIT License

```

Let me know if you'd like this tailored further for Docker, environment variables, or deployment.
```
