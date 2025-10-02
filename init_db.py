import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()

USER = os.getenv("MYSQL_USER")
PASSWORD = os.getenv("MYSQL_PASSWORD")
HOST = os.getenv("MYSQL_HOST")
DB = os.getenv("MYSQL_DB")

engine = create_engine(f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}")

print(f"************{engine}")
with engine.connect() as conn:

    conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {DB}"))

    print(f" Base de données '{DB}' créée (ou déjà existante).")
