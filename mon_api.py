from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def accueil():
    return {"message": "Bienvenue sur mon API crypto"}

@app.get("/bitcoin")
def prix_bitcoin():
    return {"crypto": "Bitcoin", "prix": 80000, "devise": "USD"}

import requests 

@app.get("/prix/{crypto}")
def prix_live(crypto: str): 
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies=usd"
    data = requests.get(url).json()
    return data
