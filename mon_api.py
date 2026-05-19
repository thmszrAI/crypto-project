from fastapi import FastAPI
import requests
import pandas as pd 

app = FastAPI()

@app.get("/")
def accueil ():
    return {"message": "Bienvenue sur mon API cypto !"}
          
@app.get("/prix/{crypto}")
def prix_live(crypto: str):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies=usd"
    data = requests.get(url).json()
    return data 

@app.get("/portfolio")
def portfolio():
    try:
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,bittensor,chainlink,kaspa&vs_currencies=usd"
        data = requests.get(url).json()
        if "status" in data : 
            return {"erreur": "Limite API CoinGecko atteinte, réessaie dans quelques minutes"}
                        
        positions = [
            {"crypto": "BTC", "quantite": 20, "prix": data["bitcoin"]["usd"]},
            {"crypto": "ETH", "quantite": 10, "prix": data["ethereum"]["usd"]},
            {"crypto": "TAO", "quantite": 10, "prix": data["bittensor"]["usd"]},
            {"crypto": "LINK", "quantite": 5, "prix": data["chainlink"]["usd"]},
            {"crypto": "KASPA", "quantite": 100, "prix": data["kaspa"]["usd"]},
        ]
        df = pd.DataFrame(positions)
        df["valeur"] = df["quantite"] * df["prix"]
        total = df["valeur"].sum()
        return {"portfolio": positions,"total_usd": round(total, 2)}
    except Exception as e: 
        return {"erreur": str(e)}