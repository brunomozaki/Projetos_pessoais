import psycopg2
import os
from pathlib import Path
from dotenv import load_dotenv
import csv



env_path = Path('amazon_ds_books/.env')        # Reads from .env file so that the token doesnt need to be written on the script
load_dotenv(dotenv_path= env_path)

conn = psycopg2.connect(database="amazon_ds",
                        user= os.environ['POST_USER'], password=  os.environ['POST_PASS'],
                        host='localhost', port='5432'
)

cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS DS_BOOKS(
    DESCRIPTION varchar(255),
    PRICE varchar(255),
    RATING varchar(255),
    REVIEW_COUNT  INTEGER,
    URL varchar
)
 """)
conn.commit()

with open('amazon_ds_books/ds_books_results.csv', 'r') as f:
    next(f, None) 
    cur.copy_from(f, 'DS_BOOKS', columns=('DESCRIPTION', 'PRICE', 'RATING', 'REVIEW_COUNT', 'URL'), sep=';', null= '')

conn.commit()