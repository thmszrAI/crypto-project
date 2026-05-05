import pandas as pd 
import matplotlib.pyplot as plt 
df=pd.read_csv("crypto.csv")
df["valeur"]=df["quantite"] * df["prix"]

plt.pie(df["valeur"], labels=df["crypto"], autopct="1.1f%%")
plt.title("Mon Portfolio Crypto")
plt.show()