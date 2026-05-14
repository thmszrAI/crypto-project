import time
import subprocess

print("Démarrage du tracker automatique...")
print("Prix mis à jour toutes les heures. Ctrl+C pour arrêter.")

while True: 
    subprocess.run(["python3", "/Users/toma/portfolio_live.py"])
    print("Prochain update dans 1 heure...")
    time.sleep(3600)