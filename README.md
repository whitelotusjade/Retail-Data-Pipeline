# Retail Data ETL Pipeline

## Overview

This project is an end-to-end ETL (Extract, Transform, Load) pipeline built with Python. It extracts retail product and user data from a REST API, transforms the data into a clean and structured format using pandas, and loads it into a PostgreSQL database.

The project demonstrates fundamental data engineering concepts including REST API integration, JSON processing, data transformation, and loading data into a relational database using a modular ETL workflow.

---

## Tech Stack

* Python
* pandas
* requests
* SQLAlchemy
* PostgreSQL

---

## ETL Workflow

### Extract

* Connect to the REST API.
* Retrieve product and user data.
* Convert the JSON response into pandas DataFrames.

### Transform

* Rename columns with descriptive names.
* Select only the required columns.
* Convert data types where needed.
* Extract nested JSON fields (first name, last name, street, city, and zipcode) into separate columns.

### Load

* Connect to a PostgreSQL database using SQLAlchemy.
* Create or replace database tables.
* Load the transformed data into PostgreSQL.

---

## Project Structure

```text
retail-data-etl-pipeline/
│
├── etl/
│   ├── extract.py      # Extract data from the REST API
│   ├── transform.py    # Clean and transform the data
│   └── load.py         # Load data into PostgreSQL
│
├── main.py             # Execute the ETL pipeline
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation
```

---

## Database Tables

The pipeline creates the following PostgreSQL tables:

* `products`
* `users`

---

## Pipeline Architecture

```text
REST API
    │
    ▼
Extract
    │
    ▼
Transform (pandas)
    │
    ▼
Load (PostgreSQL)
```

---

## Data Source

This project uses retail product and user data from the **Fake Store API**.

**Website:** https://fakestoreapi.com/

**API Endpoints:**

* Products: `https://fakestoreapi.com/products`
* Users: `https://fakestoreapi.com/users`

---

## Skills Demonstrated

* REST API integration
* JSON processing
* Data extraction
* Data transformation with pandas
* Data cleaning
* PostgreSQL
* SQLAlchemy
* ETL pipeline development
* Modular Python programming

---

## Prerequisites

Before running the project, ensure you have:

* Python 3.x
* PostgreSQL installed and running
* A PostgreSQL database created (e.g., `fake_store_db`)

Install the required Python packages:

```bash
pip install -r requirements.txt
```

---

## Configuration

Update the PostgreSQL connection details in `etl/load.py` before running the project.

```python
host = "localhost"
port = 5432
user = "postgres"
password = "<YOUR_PASSWORD>"
db_name = "fake_store_db"
```

---

## How to Run

1. Clone this repository.
2. Create a PostgreSQL database named `fake_store_db`.
3. Update the database credentials in `etl/load.py`.
4. Install the project dependencies:

```bash
pip install -r requirements.txt
```

5. Run the ETL pipeline:

```bash
python main.py
```

After the pipeline finishes, the `products` and `users` tables will be created and populated in PostgreSQL.

---



