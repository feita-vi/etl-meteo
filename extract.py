import requests
import os
from dotenv import load_dotenv


load_dotenv()

def extract(city):

    api_key = os.getenv("API_KEY")

    if not api_key:
        raise Exception("API_KEY non trouvée. Vérifie ton fichier .env")
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    response = requests.get(url)
    
    if response.status_code != 200:
        raise Exception(f"Erreur API : {response.status_code} {response.text}")
    
    
    return response.json()




