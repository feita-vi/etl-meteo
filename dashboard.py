import os
import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

USER = os.getenv("MYSQL_USER")
PASSWORD = os.getenv("MYSQL_PASSWORD")
HOST = os.getenv("MYSQL_HOST")
DB = os.getenv("MYSQL_DB")


if not all([USER, PASSWORD, HOST, DB]):
    st.error(" Impossible de charger les variables de connexion MySQL. Vérifie ton fichier .env.")
else:
    st.title("🌦️ Dashboard Météo - Bordeaux")

engine = create_engine(f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}/{DB}")

df = pd.read_sql("SELECT * FROM meteo", engine)

st.subheader("📊 Dernières données")
st.write(df.tail())

st.subheader("📈 Evolution température et humidité")
st.line_chart(df[["temperature", "humidite"]])
