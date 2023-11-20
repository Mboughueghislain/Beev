import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Charge les variables d'environnement depuis le fichier .env
load_dotenv()

# Configuration de la base de données
db_config = {
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'port': os.getenv('DB_PORT'),
    'database': os.getenv('DB_DATABASE')
}


# Création de la connexion à la base de données PostgreSQL
engine = create_engine(f"postgresql+psycopg2://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}")

# Écriture d'une requête SQL pour récupérer les données 
query = "SELECT * FROM car"
query2 = "SELECT * FROM consumer"


# Lecture des données de la base de données et affectation dans un DataFrame pandas
df_car = pd.read_sql_query(query, engine)
df_consumer = pd.read_sql_query(query2, engine)

# Affichage des données
print(df_car)
print(df_consumer)