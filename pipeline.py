from extract import extract
from transform import transform
from load import load

def run_pipeline(city="Bordeaux"):
    
    data = extract(city)
    df = transform(data)
    load(df)

    return df

if __name__ == "__main__":

    result = run_pipeline("Bordeaux")
    
    print(result)
