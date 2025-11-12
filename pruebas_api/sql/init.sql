/*
pruebas_api/sql/init.sql
Script SQL para inicializar la base de datos y el usuario para pruebas
Crear la base de datos y el usuario
*/
CREATE DATABASE qa_db;
/* Crear un usuario con privilegios para la base de datos de pruebas */
CREATE USER qa_user WITH ENCRYPTED PASSWORD 'qa_pass';
/* Conceder todos los privilegios al usuario en la base de datos de pruebas */
GRANT ALL PRIVILEGES ON DATABASE qa_db TO qa_user;
/* Fin de init.sql */