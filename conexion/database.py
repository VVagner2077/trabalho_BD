# conexion/database.py

import psycopg2
import os
from psycopg2 import OperationalError
from dotenv import load_dotenv

def criar_conexao():
    """
    cria uma conexao com o banco de dados PostgreSQL hospedado no Aiven.
    """
    load_dotenv()
    db_url = os.getenv("DB_PASSWORD")

    try:
        conexao = psycopg2.connect(db_url)
        print("Conexão bem-sucedida ao banco de dados PostgreSQL")
        return conexao
    except OperationalError as err:
        print(f"Erro ao se conectar ao bando de dados Erro: {err}")
        return None
        
criar_conexao()