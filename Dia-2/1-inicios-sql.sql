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

-- NOTA: SIEMPRE EN LOS UPDATES Y DELETES TENEMOS QUE EJECUTARLOS CON UNA CONDICIONAL
-- DELETE
DELETE FROM alumnos WHERE id>=10 AND id <=12;

SELECT * FROM alumnos;

-- UPDATE tabla SET columna='Nuevo valor' WEHRE condicional
UPDATE alumnos SET nombre='Marimar' WHERE id = 8;
UPDATE alumnos SET num_documento = '99564879', nombre = 'Rodrigo' WHERE id= 9 ;

SELECT * FROM alumnos;

INSERT INTO alumnos (nombre, sexo, num_documento, fecha_nacimiento) VALUES
					('Maria aLEJANDRA', 'BINARIX', '49596785', '1995-06-19');
                    
SELECT * FROM alumnos;

-- 1. Mostrar todos los alumnos que tengan C.E.
SELECT * FROM alumnos WHERE tipo_documento = 'C.E.';

-- 2. Mostrar a todos los alumnos que tengan SEXO MASCULINO O FEMENINO
SELECT * FROM alumnos WHERE sexo = 'MASCULINO' OR sexo = 'FEMENINO';
SELECT * FROM alumnos WHERE sexo in ('MASCULINO', 'FEMENINO');

-- 3. Mostrar a todos los alumnos que nacieron antes del 1990-01-01
SELECT * FROM alumnos WHERE fecha_nacimiento < '1990-01-01';

-- Dame todos los alumnos cuyo nombre contenga la letra a
SELECT nombre FROM alumnos WHERE nombre like '%a%';

-- Dame todos los alumnos cuya ultima letra sea la a
-- Con la propiedad BINARY le indicamos que haga la comparacion a nivel de binarios 
SELECT nombre FROM alumnos WHERE nombre LIKE BINARY '%A';
SELECT nombre FROM alumnos WHERE nombre like '%a';

SELECT nombre FROM alumnos WHERE nombre LIKE '%d%u%';

-- Dame todos los alumnos cuya segunda letra sea la o
SELECT nombre FROM alumnos WHERE nombre LIKE '_o%';

-- SELECT nombre FROM alumnos WHERE nombre LIKE 'E__%'; (E al inicio y dos espacios después)
SELECT nombre FROM alumnos WHERE nombre LIKE '%d%u%';
SELECT nombre FROM alumnos WHERE nombre LIKE '%d_u%';

-- 4. Mostrar todos los alumnos cuyo nombre tenga al menos la letra 'n'
SELECT nombre FROM alumnos WHERE nombre LIKE '%n%';

-- 5. Mostrar todos los alumnos cuyo segundo dígito del documento sea '8'
SELECT num_documento FROM alumnos WHERE num_documento LIKE '_8%';

-- 6. Mostrar todos los alumnos cuyo sexo contenga la letra 'i' seguido de una letra cualquiera y luego la letra 'o'
SELECT sexo FROM alumnos WHERE sexo LIKE '%i_o';

-- (cualquier parte tenga la i y la última tenga 0)
SELECT sexo FROM alumnos WHERE sexo LIKE '%i%o'; 