# Este es un proyecto de ejemplo para una API RESTful simple usando Flask y PostgreSQL, 
# realizando operaciones básicas de registro y login de usuarios, además de verificar el estado de la API. 
# Utiliza solo paquetes públicos disponibles en el ecosistema de Python. 
# Las pruebas unitarias y de integración se implementan utilizando pytest y requests.
# para ejecutar las pruebas automáticamente al iniciar el contenedor Docker.
# se incluye un archivo Dockerfile para construir la imagen del contenedor.
# la ruta para ejecutar la aplicación es /app.py
# docker exec -it qa_api_test /app.py
#pruebas_api/backend/app.py
 
# Archivo principal de la aplicación Flask que define las rutas y la lógica de la API.

from flask import Flask, request, jsonify
from db import get_db, create_tables
# Configuración de la aplicación Flask
app = Flask(__name__)
# Inicialización de la base de datos al iniciar la aplicación
@app.before_request
def init_db_once():
    if not hasattr(app, 'db_initialized'):
        create_tables()
        app.db_initialized = True

# Ruta para registrar un nuevo usuario
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
# Validación básica de los datos recibidos
    if not email or not password:
        return jsonify({'error': 'Campos requeridos'}), 400
# Verificación si el usuario ya existe
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE email=%s;", (email,))
    if cur.fetchone():
        return jsonify({'error': 'Usuario ya registrado'}), 400
    cur.execute("INSERT INTO users (email, password) VALUES (%s, %s);", (email, password))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'message': 'Usuario registrado correctamente'}), 201

# Ruta para el login de usuarios
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
# Validación básica de los datos recibidos
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE email=%s AND password=%s;", (email, password))
    user = cur.fetchone()
    cur.close()
    conn.close()
# Verificación de credenciales
    if not user:
        return jsonify({'error': 'Credenciales inválidas'}), 401
    return jsonify({'message': 'Login exitoso'}), 200

# Ruta para verificar el estado de la API
@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'}), 200

# Ejecución de la aplicación Flask
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

# Fin de app.py