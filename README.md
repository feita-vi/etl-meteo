#  Projet ETL Météo (Python + MySQL + Streamlit)

## 🎯 Objectif
Ce projet illustre un pipeline **ETL (Extract - Transform - Load)** construit en Python pour :
- Extraire des données météo en temps réel depuis l'API **OpenWeather**,
- Transformer les données en format exploitable (Pandas DataFrame),
- Charger les résultats dans une base **MySQL**,
- Visualiser les tendances via un **dashboard interactif (Streamlit)**.

Ce projet démontre mes compétences en **Data Engineering** : API, Python, Pandas, SQL, ETL, Visualisation et Gestion d’environnement.

---

## 🛠️ Technologies utilisées
- **Python 3.10+**
- **Pandas** (manipulation de données)
- **Requests** (appel API)
- **SQLAlchemy + PyMySQL** (connexion MySQL)
- **Streamlit** (dashboard interactif)
- **python-dotenv** (gestion des variables d'environnement)

---

## 📂 Structure du projet

etl_meteo/
├── extract.py # Extraction depuis l'API OpenWeather
├── transform.py # Transformation JSON -> DataFrame
├── load.py # Chargement dans MySQL
├── pipeline.py # Orchestration ETL
├── dashboard.py # Dashboard Streamlit
├── init_db.py # Création de la base MySQL
├── requirements.txt # Dépendances
├── .env # Variables d'environnement (non versionné)
└── README.md # Documentation

---

## ⚙️ Installation & Setup

### 1️⃣ Cloner le repo
```bash
git clone https://github.com/mon-github/etl_meteo.git
cd etl_meteo
```
### 2️⃣ Créer un environnement virtuel
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```
### 3️⃣ Installer les dépendances
```bash
pip install -r requirements.txt
```
### 4️⃣ Configurer les variables d'environnement

Créer un fichier .env :

API_KEY=ta_cle_openweather
MYSQL_USER=root
MYSQL_PASSWORD=motdepasse
MYSQL_HOST=localhost
MYSQL_DB=meteo_db

## 🚀 Utilisation

### 1️⃣ Créer la base MySQL
```bash
python init_db.py
```
### 2️⃣ Lancer le pipeline ETL
```bash
python pipeline.py
```
Les données météo seront insérées dans la base **meteo_db, table meteo.**

### 3️⃣ Visualiser avec Streamlit
```bash
streamlit run dashboard.py
```
Puis ouvre http://localhost:8501 dans ton navigateur.

---

## ⏱️ Automatisation

Le pipeline peut être exécuté automatiquement grâce à un ordonnanceur :

- **Linux/Mac (cron)** :  
```
0 * * * * /usr/bin/python3 /home/ton_user/etl_meteo/pipeline.py >> /home/ton_user/etl_meteo/logs/etl.log 2>&1
```
0 * * * * /usr/bin/python3 C:\Users\yvann\Documents\EFREI_COURS\PYTHON\etl_meteo/pipeline.py >> /home/ton_user/etl_meteo/logs/etl.log 2>&1
- **Windows (Planificateur de tâches)** :  
```
python C:\Users\...\...\etl_meteo\pipeline.py
```
Suppression : retirer la ligne cron (crontab -e) ou supprimer la tâche Windows.

## 👩‍💻 Auteur
Projet réalisé par **FEITAMA Vianelle** – Étudiant(e) Data Engineering, en M1 Data et IA à l'EFREI en recherche d’alternance à Bordeaux.






