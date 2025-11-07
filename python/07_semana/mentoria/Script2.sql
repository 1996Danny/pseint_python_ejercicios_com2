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

-- Nueva Tabla

CREATE TABLE estudiantes (
    id_estudiante INT PRIMARY KEY,
    nombre VARCHAR(100),
    email VARCHAR(100),
    fecha_nacimiento DATE
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

-- Datos de la nueva tabla
INSERT INTO estudiantes (id_estudiante, nombre, email, fecha_nacimiento) VALUES
(1, 'María López', 'maria.lopez@escuela.com', '2001-05-12'),
(2, 'Pedro Martínez', 'pedro.martinez@escuela.com', '2000-08-23'),
(3, 'Lucía Fernández', 'lucia.fernandez@escuela.com', '2002-11-30'),
(4, 'Sofía Torres', 'sofia.torres@escuela.com', '2003-03-15');


SELECT * FROM profesores;
SELECT id_curso AS 'ID', nombre_curso AS 'Los Cursos', descripcion FROM cursos WHERE nombre_curso LIKE '%Web%';
SELECT nombre_curso AS 'Los Cursos', descripcion FROM cursos ORDER BY nombre_curso DESC; 



SELECT id_curso AS 'ID', nombre_curso AS 'Los Cursos', descripcion, nombre AS 'Profesor', email AS 'Email' FROM cursos
INNER JOIN profesores ON cursos.id_profesor = profesores.id_profesor
;

CREATE TABLE inscripciones (
id_inscripcion INT PRIMARY KEY AUTO_INCREMENT,
id_estudiante INT,
id_curso INT,
fecha_inscripcion DATE,
FOREIGN KEY (id_estudiante) REFERENCES estudiantes(id_estudiante),
FOREIGN KEY (id_curso) REFERENCES cursos(id_curso)
);

INSERT INTO inscripciones (id_estudiante, id_curso, fecha_inscripcion) VALUES
(1, 1, '2025-10-01'),
(2, 2, '2025-10-02'),
(3, 3, '2025-10-03'),
(4, 1, '2025-10-04'),
(4, 2, '2025-10-05');

SELECT * FROM inscripciones


-- QUIERO CAMBIAR EL EMAIL DE UN ESTUDIANTE
UPDATE estudiantes
SET email = 'lucia.f@escuela.com'
WHERE id_estudiante = 3;

SELECT * FROM estudiantes

-- QUIERO CAMBIAR EL PROFESOR ASIGNADO AL CURSO DE DESARROLLO WEB
UPDATE cursos -- Donde quiero modificar
SET id_profesor = 4 -- El valor que quiero que quede en la columna.
WHERE id_curso = 4; -- En qué registro quiero que se modifique el valor.

SELECT * FROM cursos

-- QUIERO ELIMINAR UNA INSCRIPCION
DELETE FROM inscripciones -- De donde quiero eliminar
WHERE id_inscripcion = 2; -- Qué registro/s quiero eliminar;


-- USO TRANSACTION Y COMMIT
START TRANSACTION;

INSERT INTO inscripciones (id_estudiante, id_curso, fecha_inscripcion)
VALUES (4, 2, '2025-11-06');

UPDATE cursos
SET cupo_disponible = cupo_disponible - 1
WHERE id_curso = 2;

COMMIT;

select * from inscripciones






