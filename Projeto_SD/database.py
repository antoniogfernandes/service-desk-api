import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.getenv("MYSQL_DB")

DB_CONFIG = {
    "host": os.getenv("MYSQL_HOST"),
    "user": os.getenv("MYSQL_USER"),
    "password": os.getenv("MYSQL_PASSWORD"),
    "port": int(os.getenv("MYSQL_PORT"))
}


def teste_conexao():
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        print("Conexão com MySQL realizada com sucesso!")
        connection.close()
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")


def conectar_sem_banco():
    return mysql.connector.connect(**DB_CONFIG)


def conectar_com_banco():
    config = DB_CONFIG.copy()
    config["database"] = DB_NAME
    return mysql.connector.connect(**config)


def criar_banco():
    conn = conectar_sem_banco()
    cursor = conn.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
    conn.commit()
    cursor.close()
    conn.close()
    print(f"Banco '{DB_NAME}' criado/verificado com sucesso!")


def criar_tabelas():
    conn = conectar_com_banco()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            setor VARCHAR(100) NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS chamados (
            id INT AUTO_INCREMENT PRIMARY KEY,
            titulo VARCHAR(150) NOT NULL,
            descricao TEXT NOT NULL,
            prioridade ENUM('Baixa','Média','Alta') NOT NULL,
            status ENUM('Aberto','Em Atendimento','Concluído') DEFAULT 'Aberto',
            setor VARCHAR(100) NOT NULL,
            data_abertura DATETIME DEFAULT CURRENT_TIMESTAMP
            )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS atendimentos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            descricao TEXT NOT NULL,
            data_atendimento DATETIME DEFAULT CURRENT_TIMESTAMP,
            chamado_id INT,
            FOREIGN KEY (chamado_id) REFERENCES chamados(id)
        )
    """)

    cursor.execute("SHOW TABLES")
    tabelas = cursor.fetchall()

    print("Tabelas no banco:")
    for tabela in tabelas:  
        print("-", tabela[0])

    conn.commit()
    cursor.close()
    conn.close()

    print("Tabelas criadas/verificadas com sucesso!")

    


def inicializar_banco():
    criar_banco()
    criar_tabelas()


if __name__ == "__main__":
    inicializar_banco()
