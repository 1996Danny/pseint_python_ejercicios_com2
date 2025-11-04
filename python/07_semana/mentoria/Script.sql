CREATE DATABASE universidad;
USE universidad;
CREATE TABLE profesores (
	id_profesor INT PRIMARY KEY,
	nombre VARCHAR(100),
	email VARCHAR(100),
	telefono VARCHAR(20),
);
CREATE TABLE cursos (
	id_curso INT PRIMARY KEY,
	nombre_curso VARCHAR (100),
	descripcion TEXT,
	id_profesor INT,
	FOREIGN KEY (id_profesor) REFERENCES profesores(id_profesor)
);

INSERT INTO profesores (id_profesor, nombre, email, telefono) VALUES
(1, 'Juan Perez', 'juan.perez@escuela.com', '123-456-7890'),
(2, 'Ana Gómez', 'ana.gomez@escuela.com', '098-765-4321'),
(3, 'Carlos Ruiz', 'carlos.ruiz@escuela.com', '555-555-5555'),
(4, 'Infor Matorio', 'infor.matorio@escuela.com', '635-424-1240');

INSERT INTO cursos (id_curso, nombre_curso, descripcion, id_profesor) VALUES
(1, 'Matemáticas Avanzadas', 'Curso de matemáticas para nivel avanzado', 1),
(2, 'Literatura Española', 'Estudio de la literatura de España', 2),
(3, 'Programación en Python', 'Introducción a la programación en Python', 3),
(4, 'Desarrollo Web', '2da etapa Base de datos', NULL);

SELECT * FROM profesores;
SELECT id_curso AS 'ID', nombre_curso AS 'Los Cursos', descripcion FROM cursos WHERE nombre_curso LIKE '%Web%';
SELECT nombre_curso AS 'Los Cursos', descripcion FROM cursos ORDER BY nombre_curso DESC; 



SELECT id_curso AS 'ID', nombre_curso AS 'Los Cursos', descripcion, nombre AS 'Profesor', email AS 'Email' FROM cursos
INNER JOIN profesores ON cursos.id_profesor = profesores.id_profesor
;


