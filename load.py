# Import the function used to connect to a database
from sqlalchemy import create_engine

# PostgreSQL connection details
host = "localhost"
port = 5432
user = "postgres"
password = "SQLpass123."
db_name = "fake_store_db"  # Create this database before running


def load_to_postgres(df, table_name):
    # Connect to the PostgreSQL database
    engine = create_engine(
        f"postgresql://{user}:{password}@{host}:{port}/{db_name}"
    )

    # Load the DataFrame into a PostgreSQL table
    df.to_sql(
        table_name,
        engine,
        if_exists="replace",  # Replace the table if it already exists
        index=False           # Don't save DataFrame row numbers
    )

