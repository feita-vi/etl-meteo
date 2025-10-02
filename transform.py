import pandas as pd
from datetime import datetime

def transform(data):

    df = pd.DataFrame([{

        "ville": data["name"],
        "temperature": data["main"]["temp"],
        "humidite": data["main"]["humidity"],
        "description": data["weather"][0]["description"],
        "datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S") 

    }])

    return df