import pandas as pd 

data = { 
    "crypto": ["BTC", "ETH", "TAO"], 
    "quantite": [21, 10, 10],
    "prix": [78000, 2350, 300]
}
df = pd.DataFrame(data)
print(df)
df["valeur"] = df["quantite"] * df["prix"]
print(df)
print("total wallet :", df["valeur"].sum(),"$")

gros_positions = df[df["valeur"]> 10000]
print(gros_positions)
print (df[df["prix"] == df["prix"].max()])
print(df.sort_values("valeur", ascending=False))
print(df["valeur"].mean())
print(df["valeur"].max())
print(df["valeur"].min())
print(df.describe())
