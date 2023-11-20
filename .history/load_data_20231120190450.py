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

# Chemin vers les fichiers CSV
csv_file_path = '/home/ghislain/Bureau/Beevn/car_data.csv'
csv_file_path2 = '/home/ghislain/Bureau/Beevn/consumer_data.csv'

# Chargement des fichiers CSV dans les DataFrames
df = pd.read_csv(csv_file_path)
df2 = pd.read_csv(csv_file_path2)

# Création de la une connexion à la base de données PostgreSQL
engine = create_engine(f"postgresql+psycopg2://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}")

# Chargement du DataFrame dans la base de données
df.to_sql('car', engine, index=False, if_exists='replace')  # 'replace' pour remplacer la table existante
df2.to_sql('consumer', engine, index=False, if_exists='replace')  # 'replace' pour remplacer la table existante

# Impression du résultat dans la console
print("Chargement terminé.")
