# Import Libraries
from dotenv import load_dotenv
import psycopg2
import os
import csv
import io

csv_filepath = os.getenv('csv_path')
table_name = 'econometrics'

def connect_to_db():                            # Establish Connection to Database
    load_dotenv()
    return psycopg2.connect(
        host = os.getenv('DB_HOST'),
        database = os.getenv('DB_NAME'),
        user =os.getenv('DB_USER'),
        password = os.getenv('DB_PASSWORD'),
        port = os.getenv('DB_PORT')
    )

def ingest_data():                              # Main Function Ingesting Data
    try:
        # Connect to PostgreSQL
        conn = connect_to_db()
        curr = conn.cursor()

        # Create The Table in PostgreSQL
        curr.execute("""
                    DROP TABLE IF EXISTS econometrics;
                    CREATE TABLE econometrics(
                                    year varchar,
                                    gdp float,
                                    inflation float,
                                    unemployment float);""")
        conn.commit()

        # Open the CSV file and create a file-like object
        with open(csv_filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            csv_data = io.StringIO("".join(lines[1:]))  # skip first line
            curr.copy_from(csv_data, table_name, sep=',', null='')
        conn.commit()
        print(f"Data successfully imported from {csv_filepath} into {table_name}.")

    except psycopg2.Error as e:
        print(f"Error importing data: {e}")
        conn.rollback()

    finally:
        if conn:
            curr.close()
            conn.close()

if __name__ == "__main__":
    ingest_data()