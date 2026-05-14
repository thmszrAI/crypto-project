import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv("/Users/toma/historique.csv")

btc = df[df["crypto"] == "BTC"]

plt.figure(figsize=(10, 5))
plt.plot(btc["date"], btc["valeur"], marker="o")
plt.title("Évolution BTC dans le portfolio")
plt.xlabel("Date")
plt.ylabel("Valeur ($)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()