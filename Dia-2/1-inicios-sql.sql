-- Esto es un comentario

-- SQL (Structured Query Languaje) Lenguaje Estructurado de Consultas
-- EN SQL siempre hay que colocar el ';' al final de cada query
-- Dos Sub lenguajes de manejo de informacion
-- DDL (Data Definition Languaje) > Lenguaje de Definicion de Datos

-- CREATE
CREATE DATABASE pruebas;

-- Sirve para listar las bases de datos que hay en este servidor
SHOW DATABASES;

-- Seleccionar la base e datos que vamos a trabajar
USE pruebas;

-- Siempre las pabras reservadas se recomiendan que se coloquen en mayusculas
-- Las tablas siempre deben tener nombres pluralizados
CREATE TABLE alumnos(
	-- Ahora definimos las columnas
    -- nombre_col tipo_dato [parametros opcionales]
    id INT PRIMARY KEY AUTO_INCREMENT,
    NOMBRE VARCHAR(100) NOT NULL,
    -- es un tipo de dato que permite guardar determinados valores
    sexo ENUM('FEMENINO', 'MASCULINO', 'BINARIX', 'OTRO', 'HELICÓPTERO'),
    -- agregar la columna tipo_documento que soamente puede ser DNI, C.E., PASAPORTE
    -- y la columna num_documento que solamente puede tener hasta 10 caracteres
    tipo_documento ENUM('DNI', 'C.E.', 'PASAPORTE') DEFAULT 'DNI',
    num_documento VARCHAR(10) NOT NULL,
    fecha_nacimiento DATETIME
);

-- Para ver las tablas en la terminal
SHOW TABLES;

-- DML (Data Manipulation Lagunage)
-- Lenguaje de Manupulación de Datos

-- SELECT [columnas] FROM tabla;
SELECT nombre, sexo FROM alumnos;
SELECT * FROM alumnos;

-- INSERT INTO tabla (columnas) VALUES (valores)
INSERT INTO alumnos (nombre, sexo, num_documento, fecha_nacimiento) VALUES
					('Eduardo', 'MASCULINO', '73500746', '1992-08-01');
                    
INSERT INTO alumnos (nombre, sexo, num_documento, fecha_nacimiento) VALUES
					('Ronald', 'BINARIX', '75268256', '1995-07-25'),
                    ('Karim', 'FEMENINO', '85234716', '1991-01-15'),
                    ('Alexa', 'HELICOPTERO', '14729583', '1995-06-08');
                    
SELECT * FROM alumnos;

INSERT INTO alumnos VALUES
					(DEFAULT, 'Romina', 'FEMENINO', 'C.E.', '456789123', '1987-05-14'),
                    (DEFAULT, 'Roberto', 'BINARIX', 'PASAPORTE', '15946789', '1985-01-01'),
                    (DEFAULT, 'Jair', 'MASCULINO', DEFAULT, '34598746', '1995-04-09');

SELECT * FROM alumnos;