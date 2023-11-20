import pandas as pd
from sqlalchemy import create_engine

# Chargement des informations de configuration de la base de donnée
db_config = {
    'user': 'admin',
    'password': 'admin',
    'host': 'localhost',
    'port': '5432',
    'database': 'test_db'
}

# Chemin vers mes fichiers CSV
csv_file_path = '/home/ghislain/Bureau/Beevn/car_data.csv'
csv_file_path2 = '/home/ghislain/Téléchargements/Beev/consumer_data.csv'

# Chargement des fichiers CSV dans les DataFrames
df = pd.read_csv(csv_file_path)
df2 = pd.read_csv(csv_file_path2)

# Création de la une connexion à la base de données PostgreSQL
engine = create_engine(f"postgresql+psycopg2://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}")

# Chargement du DataFrame dans la base de données
df.to_sql('car', engine, index=False, if_exists='replace')  # 'replace' pour remplacer la table existante
df2.to_sql('consumer', engine, index=False, if_exists='replace')  # 'replace' pour remplacer la table existante

print("Chargement terminé.")
