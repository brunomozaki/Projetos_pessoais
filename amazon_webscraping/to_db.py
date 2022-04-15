import psycopg2
import os
from pathlib import Path
from dotenv import load_dotenv
import csv



env_path = Path('amazon_webscraping/.env')        # Reads from .env file so that the token doesnt need to be written on the script
load_dotenv(dotenv_path= env_path)

conn = psycopg2.connect(database="amazon_ds",
                        user='postgres', password=  os.environ['POST_PASS'],
                        host='localhost', port='5432'
)

cur = conn.cursor()
cur.execute("""
    CREATE TABLE IF NOT EXISTS DS_BOOKS(
    DESCRIPTION TEXT,
    PRICE TEXT,
    RATING TEXT,
    REVIEW_COUNT INTEGER,
    URL VARCHAR
)
 """)
conn.commit()

with open('amazon_webscraping/results.csv', 'r') as f:
    next(f) 
    cur.copy_from(f, 'DS_BOOKS', columns=('DESCRIPTION', 'PRICE', 'RATING', 'REVIEW_COUNT'), sep=';')

conn.commit()

#columns=('DESCRIPTION', 'PRICE', 'RATING', 'REVIEW_COUNT')