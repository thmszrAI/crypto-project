import sqlite3

conn = sqlite3.connect("/Users/toma/ecommerce.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS clients")
cursor.execute("DROP TABLE IF EXISTS commandes")

cursor.execute("""
    CREATE TABLE clients (
        id INTEGER PRIMARY KEY,
        nom TEXT,
        ville TEXT
    )
""")

cursor.execute("""
    CREATE TABLE commandes (
        id INTEGER PRIMARY KEY, 
        client_id INTEGER,
        produit TEXT, 
        montant REAL, 
        date TEXT
    )
""")

clients = [ 
    (1, "Dupont", "Geneve"),
    (2, "Martin", "Lausanne"),
    (3, "Bernard", "Geneve"),
    (4, "Petit", "Zurich"),
]

commandes = [
    (1, 1, "Laptop", 1200, "2026-01-05"),
    (2, 1, "Souris", 25, "2026-01-08"),
    (3, 2, "Clavier", 80, "2026-02-01"),
    (4, 3, "Laptop", 1200, "2026-03-02"),
    (5, 3, "Ecran", 300, "2026-03-02"),
    (6, 1, "Ecran", 300, "2026-03-10"),
    (7, 4, "Souris", 25, "2026-03-15"),
    (8, 2, "Laptop", 1200, "2026-03-20"),
]

cursor.executemany("INSERT INTO clients VALUES (?, ?, ?)", clients)
cursor.executemany("INSERT INTO commandes VALUES (?, ?, ?, ?, ?)", commandes)
conn.commit()
print("Base e-commerces créée")


print("\n--- commandes d'au moins 100---")
cursor.execute("""
               SELECT * FROM commandes 
               WHERE montant > 100
               """)
resultats = cursor.fetchall()
for row in resultats:
    print(row)

print("\n--- JOIN commandes et clients---")
cursor.execute("""
                SELECT commandes.montant, clients.nom
                FROM commandes
                JOIN clients ON commandes.client_id = clients.id
""")
resultats = cursor.fetchall()
for row in resultats:
    print(row)

cursor.execute("""
               SELECT clients.nom, COUNT(*)
               FROM commandes
               JOIN clients ON commandes.client_id = clients.id
               GROUP BY clients.nom
            """)
resultats = cursor.fetchall()
for row in resultats:
    print(row)

cursor.execute("""
               SELECT clients.ville, SUM(montant)
               FROM commandes
               JOIN clients ON commandes.client_id = clients.id
               GROUP BY clients.ville
               """)
resultats = cursor.fetchall()
for row in resultats:
    print(row)
               



  
               
