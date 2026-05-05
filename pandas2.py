import pandas as pd

df = pd.read_csv("crypto.csv")
print(df)
df["valeur"] =df["quantite"] * df["prix"]
print(df)
print("Total :",df["valeur"].sum(), "$")
print(df.sort_values("valeur", ascending=False))
print(df[df["valeur"] >1000])
df["pct"] = (df["valeur"] / df["valeur"].sum() * 100).round(2)
print(df)
df.to_csv("portfolio_final.csv", index=False)
print("Fichier sauvegardé !")
print(df.groupby("crypto")["valeur"].sum())