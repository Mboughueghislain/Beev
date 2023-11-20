import pandas as pd
from sqlalchemy import create_engine

# Configuration de la base de données
db_config = {
    'user': 'admin',
    'password': 'admin',
    'host': 'localhost',
    'port': '5432',
    'database': 'test_db'
}

# Création de la connexion à la base de données PostgreSQL
engine = create_engine(f"postgresql+psycopg2://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}")

# Écriture d'une requête SQL pour récupérer les données
query = "SELECT * FROM car WHERE Make="
query2 = "SELECT * FROM consumer"


# Lecture des données de la base de données et affectation dans un DataFrame pandas
df_car = pd.read_sql_query(query, engine)
df_consumer = pd.read_sql_query(query2, engine)

# Affichage des données
print(df_car)
print(df_consumer)