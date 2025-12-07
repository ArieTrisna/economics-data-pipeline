# 📊 Economics Data Pipeline
---
A simple, beginner-friendly data engineering pipeline that ingests Japanese economic data from CSV into a PostgreSQL database.
This project illustrates a foundational ETL workflow using Python, SQL, and PostgreSQL, making it a great starting point for anyone learning data engineering.
# 🚀 Overview
---
This project performs a basic but essential ETL process:
Extract → Read a raw CSV file
Load → Create a database table and bulk-insert data using PostgreSQL’s COPY method
Manage schema → Drop and re-create the table on each run
It is intentionally lightweight to help you build practical confidence with Python, databases, SQL, and pipeline organization.
# 📁 Project Structure
---
```bash
economics-data-pipeline/
├── data/
│   └── jpn_econ.csv               # Raw dataset
├── scripts/
│   └── ingest_csv.py              # Main ingestion script
│   └── extract.py                 # Extract data script
├── README.md                      # Project documentation
├── requirements.txt               # Python dependencies (optional)
└── .env                           # Environment variables (not included)
```
# 🧰 Tech Stack
---
Python (CSV handling, ingestion logic)
PostgreSQL (data storage)
psycopg2 (database connection + COPY ingestion)
python-dotenv (environment variable loading)
# 🔧 Setup & Installation
---
1️⃣ Clone the repo
git clone https://github.com/ArieTrisna/economics-data-pipeline.git
cd economics-data-pipeline
2️⃣ Install dependencies
If you are using a virtual environment:
pip install -r requirements.txt
3️⃣ Configure your database connection
Create a .env file:
DB_HOST=your_host
DB_NAME=your_database
DB_USER=your_username
DB_PASSWORD=your_password
DB_PORT=your_port
4️⃣ Place your CSV file
Ensure jpn_econ.csv is inside:
data/jpn_econ.csv
▶️ Running the Script
From the project root:
python scripts/ingest_csv.py
The script will:
Drop the econometrics table (if exists)
Create a fresh table schema
Read and ingest data from the CSV file
Bulk-load the data using copy_from
If everything succeeds, you'll see:
Data successfully imported from data/jpn_econ.csv into econometrics.
