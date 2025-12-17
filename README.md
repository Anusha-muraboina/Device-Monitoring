# Device Monitoring API

This project is a Django-based REST API used to monitor devices and their time-series readings.  
It allows importing device readings from a CSV file and exposes APIs to fetch the latest device status and historical summaries.

This project is designed to strictly follow the **Device Monitoring API – Submission Instructions** and is compatible with automatic evaluation.

---

## Features

- Device and Reading data models
- Unique constraint to prevent duplicate readings
- CSV-based bulk data ingestion using a Django management command
- REST APIs to:
  - List devices with latest reading
  - Fetch device reading summary with date filtering
- Handles out-of-order data correctly
- Uses SQLite (Django default database)

---

## Tech Stack

- Python 3.x
- Django 4.x
- Django REST Framework
- SQLite

---

## Project Structure

device_monitoring_full/
├── manage.py
├── requirements.txt
├── README.md
├── THOUGHTS.md
├── device_monitoring/
│ ├── init.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── monitoring/
│ ├── init.py
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ ├── serializers.py
│ └── management/
│ └── commands/
│ └── load_readings.py
└── sample_data.csv

yaml


---

## Setup Instructions

### 1. Create and activate virtual environment (recommended)

#### Windows
```
 windows:
    python -m venv env
    env\Scripts\activate

macOS/Linux:
    python3 -m venv env
    source env/bin/activate

2. Install dependencies
-----------------------

    pip install -r requirements.txt

3. Run database migrations

    python manage.py makemigrations
    python manage.py migrate
4. Load sample data (Option A – Management Command)
    Ensure sample_data.csv exists in the root directory.

    python manage.py load_readings sample_data.csv
    You should see:

    nginx
    
    Imported
5. Start the development server

    python manage.py runserver

    Server will start at:

    http://127.0.0.1:8000/
API Endpoints
1. List all devices with latest reading

    GET /api/devices/
    Example:

    curl http://127.0.0.1:8000/api/devices/

<img width="1911" height="1081" alt="Screenshot 2025-12-17 104743" src="https://github.com/user-attachments/assets/65a7f10f-1271-4c86-9cb6-291d868104eb" />

2. Device summary with optional date filter

    GET /api/devices/<id>/summary/
    With date range:
<img width="1903" height="1055" alt="Screenshot 2025-12-17 104813" src="https://github.com/user-attachments/assets/758c1f4b-bd1d-4da2-be93-d9f526e8866e" />


pgsql


GET /api/devices/<id>/summary/?from=YYYY-MM-DD&to=YYYY-MM-DD
Example:


<img width="1919" height="1003" alt="Screenshot 2025-12-17 104835" src="https://github.com/user-attachments/assets/18574931-b317-4bee-944d-89e5abdece5a" />


curl http://127.0.0.1:8000/api/devices/1/summary/?from=2025-01-01&to=2025-01-31
CSV File Format
The CSV file must follow this format exactly:

csv

device_name,timestamp,power,status
Inverter-1,2025-01-01T10:00:00,230.5,OK
Inverter-2,2025-01-01T11:00:00,0,OFFLINE
device_name: string

timestamp: ISO 8601 format

power: float (>= 0)

status: OK, OFFLINE, ERROR

Data Integrity Rules
(device, timestamp) is unique

Duplicate imports are ignored

Import command can be run multiple times safely

Readings may arrive out of order

Error Handling
Invalid date ranges (from > to) return HTTP 400

Empty datasets return empty JSON arrays

Duplicate readings are safely ignored

Notes
Authentication is not enabled (as per instructions)

CORS is not required for localhost testing

SQLite is used intentionally for simplicity

How to Verify Before Submission


python manage.py migrate
python manage.py load_readings sample_data.csv
python manage.py runserver


Then test:
=========

curl http://127.0.0.1:8000/api/devices/
curl http://127.0.0.1:8000/api/devices/1/summary/
Submission Checklist
manage.py at root level

requirements.txt included

README.md included

THOUGHTS.md included

SQLite used

API endpoints accessible under /api/

Unique constraint on (device, timestamp)

Author
Prepared for the Device Monitoring API technical assignment.

yaml


---







