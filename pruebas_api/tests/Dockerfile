# pruebas_api/tests/Dockerfile
# Dockerfile para ejecutar pruebas de API con Newman
# Imagen base
FROM node:20-alpine

# Crear directorio de trabajo
WORKDIR /app

# Instalar newman y el reporter HTML
RUN npm install -g newman newman-reporter-html

# Copiar los archivos de pruebas
COPY . .

# Comando por defecto
CMD ["newman", "run", "QA_API.postman_collection.json", "--reporters", "cli,html", "--reporter-html-export", "reports/report.html"]
# Fin de Dockerfile