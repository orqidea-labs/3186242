# pruebas_api/backend/Dockerfile
# Dockerfile para la aplicación backend de Flask
FROM python:3.12-slim
# Dockerfile para la aplicación backend de Flask
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
#  Copiar el código de la aplicación al contenedor
COPY . .
#  Exponer el puerto en el que se ejecuta la aplicación Flask
CMD ["python", "app.py"]
# Fin de Dockerfile