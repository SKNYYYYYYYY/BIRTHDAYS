
# 🎂 Birthday Celebrants API

A lightweight FastAPI application for managing birthday records in a MySQL database.

## ✨ Features

- **CRUD Operations**:
  - ✅ Add new celebrants
  - 🔍 Search celebrants by name
  - 📅 View celebrants by month
  - ❌ Delete celebrants

## 🛠 Tech Stack

| Component       | Technology |
|-----------------|------------|
| Framework       | FastAPI    |
| Server         | Uvicorn    |
| Database       | MySQL      |

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- MySQL Server

### Installation
```bash
git clone https://github.com/SKNYYYYYYYY/BIRTHDAYS.git
cd BIRTHDAYS
```

### Database Setup
1. Create MySQL database:
```sql
CREATE DATABASE birthdays;
USE birthdays;

CREATE TABLE whole_year (
    id INT AUTO_INCREMENT PRIMARY KEY,
    month VARCHAR(20),
    generation VARCHAR(20),
    date VARCHAR(10),
    name VARCHAR(100),
    metadata TEXT
);
```

2. Configure credentials in `database.py`:
```python
connection = pymysql.connect(
    host='localhost',
    user='your_username',
    password='your_password',
    db='birthdays'
)
```

### Running the Application
```bash
python3 main.py
```

## 🌐 API Endpoints

| Endpoint | Method | Description | Parameters |
|----------|--------|-------------|------------|
| `/` | GET | Welcome message | - |
| `/month` | GET | Get celebrants by month | `month` (query) |
| `/new_celebrant` | POST | Add new celebrant | JSON body |
| `/search` | GET | Search by name | `name` (query) |
| `/delete` | DELETE | Delete celebrant | `name` (query) |

## 📝 Examples

### Add Celebrant
```bash
curl -X POST "http://localhost:8000/new_celebrant" \
-H "Content-Type: application/json" \
-d '{
    "month": "June",
    "generation": "4th",
    "date": "21st",
    "name": "Kip",
    "metadata": "s/o Newton"
}'
```

### Search Celebrant
```bash
curl "http://localhost:8000/search?name=kip"
```


