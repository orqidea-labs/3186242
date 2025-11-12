# pruebas_api/backend/db.py
# Módulo para la gestión de la base de datos PostgreSQL
import psycopg2
from psycopg2 import sql
import os
# Función para obtener una conexión a la base de datos
def get_db():
    return psycopg2.connect(
        host=os.getenv("POSTGRES_HOST", "db"),
        port=os.getenv("POSTGRES_PORT", "5432"),
        dbname=os.getenv("POSTGRES_DB", "postgres"),
        user=os.getenv("POSTGRES_USER", "orqidea_user"),
        password=os.getenv("POSTGRES_PASSWORD", "orqidea_password")
    )
# Función para crear las tablas necesarias en la base de datos
def create_tables():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            email VARCHAR(255) UNIQUE NOT NULL,
            password VARCHAR(255) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)
# Confirmar los cambios y cerrar la conexión
    conn.commit()
    cur.close()
    conn.close()
    print("✅ Tablas creadas o ya existentes.")
# Fin de db.py