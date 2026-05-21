# 🚀 Crypto Portfolio Tracker

Outil d'analyse de portfolio crypto en temps réel, développé en Python.

## 📊 Fonctionnalités

- Prix en temps réel via l'API CoinGecko
- Calcul automatique de la valeur du portfolio
- Historique des prix sauvegardé en CSV
- Graphiques d'évolution avec matplotlib
- API REST avec FastAPI
- Base de données SQLite

## 🛠️ Technologies utilisées

- Python 3
- pandas
- matplotlib
- FastAPI
- SQLite
- CoinGecko API

## 🚀 Lancer le projet

```bash
pip install -r requirements.txt
uvicorn mon_api:app --reload
```

## 📈 Routes API

- `GET /` — Message d'accueil
- `GET /prix/{crypto}` — Prix en temps réel
- `GET /portfolio` — Valeur totale du portfolio