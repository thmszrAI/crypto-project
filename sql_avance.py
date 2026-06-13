import sqlite3

conn = sqlite3.connect("/Users/toma/crypto.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY,
        crypto TEXT,
        type TEXT,
        montant REAL,
        date TEXT
    )
""")

conn.commit()
transactions = [
    ("BTC", "achat", 500, "2024-01-15"),
    ("ETH", "achat", 1200, "2024-01-20"),
    ("TAO", "achat", 300, "2024-02-01"),
    ("ETH", "vente", 400, "2024-02-10"),
    ("BTC", "achat", 250, "2024-03-05"),
    ("KAS", "achat", 150, "2024-03-12"),
    ("SOL", "achat", 800, "2024-04-01"),
]

cursor.execute("DELETE FROM transactions")
cursor.executemany("""
    INSERT INTO transactions (crypto, type, montant, date)
    VALUES (?, ?, ?, ?)
""", transactions)

conn.commit()
print("Données insérées avec succès")

cursor.execute("SELECT * FROM transactions")
resultats = cursor.fetchall()
for row in resultats:
    print (row)

cursor.execute("SELECT crypto, SUM(montant) FROM transactions WHERE TYPE = 'achat' GROUP BY crypto")
resultats = cursor.fetchall()
for row in resultats: 
    print (row)

cursor.execute("""
               CREATE TABLE IF NOT EXISTS prix (
               crypto TEXT,
               prix_actuel REAL
 )
""") 

cursor.execute("DELETE FROM prix")
               
prix_data = [
    ("BTC", 62000),
    ("ETH", 3000),
    ("TAO", 400),
    ("KAS", 0.15),
]
    
cursor.executemany("INSERT INTO prix VALUES (?, ?)", prix_data)
conn.commit()
print("Table prix créee et remplie")

print("\n--- JOIN transactions + prix ---")
cursor.execute("""
            SELECT transactions.crypto, transactions.type, transactions.montant, prix.prix_actuel
               FROM transactions
               JOIN prix ON transactions.crypto = prix.crypto
""")
resultats = cursor.fetchall()
for row in resultats:
    print(row)

print("\n--- JOIN transactions + prix ---")
cursor.execute("""
                SELECT transactions.crypto, transactions.type, transactions.montant, prix.prix_actuel, transactions.montant * prix.prix_actuel
               FROM transactions
               JOIN prix ON transactions.crypto = prix.crypto
               """)
resultats = cursor.fetchall()
for row in resultats:
    print(row)

cursor.execute("INSERT INTO transactions (crypto, type, montant, date) VALUES ('SOL', 'achat', 800, '2024-04-01')")
conn.commit()

print("\n--- LEFT JOIN ---")
cursor.execute("""
               SELECT transactions.crypto, transactions.type, transactions.montant, prix.prix_actuel
               FROM transactions
               LEFT JOIN prix ON transactions.crypto=prix.crypto
               """)
resultats = cursor.fetchall()
for row in resultats:
    print(row)

print("\--- VALEUR totale par crypto---")
cursor.execute("""
               SELECT transactions.crypto, SUM(transactions.montant * prix.prix_actuel)
               FROM transactions
               JOIN prix on transactions.crypto=prix.crypto
               GROUP BY transactions.crypto
               """)
resultats = cursor.fetchall()
for row in resultats:
    print(row)

print("\n--- au dessus de la moyennne---")
cursor.execute("""
               SELECT crypto, montant
               FROM transactions
               WHERE montant > (SELECT AVG(montant) FROM transactions)
""")
resultats = cursor.fetchall()
for row in resultats:
    print(row)