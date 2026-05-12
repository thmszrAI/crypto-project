import requests
import pandas as pd
pd.set_option('display.float_format', '{:.2f}'.format)
url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,chainlink,kaspa,bittensor&vs_currencies=usd"
data = requests.get(url).json()

portfolio = {
    "crypto": ["BTC", "ETH", "TAO", "LINK", "KASPA"], 
    "quantite": [20, 10, 10, 5, 100],
    "prix":[
        data["bitcoin"]["usd"],
        data["ethereum"]["usd"],
        data["bittensor"]["usd"],
        data["chainlink"]["usd"],
        data["kaspa"]["usd"]
    ]
}


df = pd.DataFrame(portfolio)
df["valeur"] = df["quantite"] * df["prix"]

print(df)
print(f"\nTotal portfolio : {df['valeur'].sum():.2f}$")

from datetime import datetime
import os 

maintenant = datetime.now().strftime("%Y-%m-%d %H: %M")
df["date"] = maintenant

if os.path.exists("/Users/toma/historique.csv"):
    df.to_csv("/Users/toma/historique.csv", mode="a", header=False, index=False)
else:
    df.to_csv("/Users/toma/historique.csv", index=False)

    print("Historique sauvegardé !")