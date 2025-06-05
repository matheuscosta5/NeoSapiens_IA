import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

# Carrega as variáveis do .env
load_dotenv()

def conectar():
    try:
        conexao = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        if conexao.is_connected():
            print("🧠 Conectado ao banco de dados com sucesso!")
            return conexao
    except Error as e:
        print(f"❌ Erro na conexão com o banco de dados: {e}")
        return None
