import sqlite3
import pandas as pd
conn = sqlite3.connect("portfolio.db")
df = pd.read_csv("crypto.csv")
df["valeur"] = df["quantite"] * df["prix"]

df.to_sql("portfolio", conn, if_exists="replace", index=False)
print("Base de données créée !")
result = pd.read_sql("SELECT SUM(valeur) as total FROM portfolio", conn)
print(result)