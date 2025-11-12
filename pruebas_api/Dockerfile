# Imagen base ligera de Node
FROM node:20-alpine

# Crea el directorio de trabajo
WORKDIR /app

# Instala Newman y el reporter HTML
RUN npm install -g newman newman-reporter-html

# Copia la colección de pruebas
COPY ./tests/postman_collection.json /app/postman_collection.json

# Crea carpeta para los reportes
RUN mkdir -p /app/reports

# Comando por defecto: ejecuta la colección con reporte HTML
CMD ["newman", "run", "postman_collection.json", "--reporters", "cli,html", "--reporter-html-export", "reports/report.html"]
