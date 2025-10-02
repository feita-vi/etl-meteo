import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

USER = os.getenv("MYSQL_USER")
PASSWORD = os.getenv("MYSQL_PASSWORD")
HOST = os.getenv("MYSQL_HOST")
DB = os.getenv("MYSQL_DB")


def load(df):

    engine = create_engine(f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}/{DB}")
   
    df.to_sql("meteo", engine, if_exists="append", index=False)

    print("Données insérées dans la base meteo.db")