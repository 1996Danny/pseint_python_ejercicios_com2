create database instituto_db;

use instituto_db;

-- comenzamos simpre por las tablas puras
-- tabla profesores --

create table profesores(
	id int primary key auto_increment not null,
    nombre varchar(40),
    dni varchar(40),
    direccion varchar(40),
    telefono varchar(40)
);

-- tabla alumnos --

create table alumnos (
	id int primary key auto_increment not null,
    n_expediente varchar(40),
    nombre varchar(40),
    apellido varchar(40), 
    fecha_nacimiento date,
    delegado bool default 0
);

-- tabla modulos --

create table modulos(
	id int primary key auto_increment not null,
    nombre varchar(40),
    id_profesor int not null,
    foreign key (id_profesor) references profesores(id)
);

-- tabla modulo_alumno --

create table modulo_alumno(
	id int primary key auto_increment not null,
    id_alumno int not null,
    id_modulo int not null,
    foreign key (id_alumno) references alumnos(id),
    foreign key (id_modulo) references modulos(id)
);

-- 3 registros para profesores --
INSERT INTO profesores (nombre, dni, direccion, telefono)
VALUES
('Juan Pérez', '30544987', 'Av. Siempre Viva 123', '1134567890'),
('María López', '28455741', 'Calle Falsa 456', '1123456789'),
('Carlos Gómez', '33789211', 'Boulevard Central 789', '1145678901');

-- mostrar los 3 registros de profesores --
SELECT * FROM profesores;

-- el profesor con el id 2 cambio su numero a 362412345678
start transaction;
SELECT * FROM profesores where id=2;
UPDATE profesores
SET telefono = '362412345678'
WHERE ID = 2;
commit;

-- 3 registros para alumnos --
INSERT INTO alumnos (n_expediente, nombre, apellido, fecha_nacimiento, delegado)
VALUES
('L0000001', 'Jose', 'Lopez', '1980-12-18', true),
('L0000002', 'Mario', 'Alvarenga', '1989-03-11', false),
('L0000003', 'Carla', 'Gimenez', '1995-02-25', false);

select * from alumnos;

-- 3 registros para modulos --
insert into modulos (nombre, id_profesor)
values ('Lengua', 1),
('Matematica', 2),
('Programacion', 3);

select * from modulos;

-- 3 registros para modulo_alumno
insert into modulo_alumno (id_alumno, id_modulo)
values (1, 3),
(2, 1),
(3, 1);

select * from modulo_alumno;
-- contar la cantidad de alumnos inscriptos al modulo 1 --
select count(id) as cantidad_alumnos from modulo_alumno where id_modulo=1;
-- obtener todos los alumnos y profesores del modulo 3 --

select p.nombre, a.nombre from profesores p, alumnos a
where p.id = (select id_profesor from modulos where id = 3)
and a.id = (select id_alumno from modulo_alumno where id_modulo = 3);

-- mostrar los alumnos ordenados por fecha de nacimiento --
select * from alumnos order by fecha_nacimiento;

-- agregar 15 registros para alumnos y para profesores
-- obtener los alumnos con un id < 7
-- obtener los profesores con un id > 5 y id < 12 ; BETWEEN
-- mostrar datos del profesor que pertenece al modulo 3
-- obtener los nombres y apellidos de los alumnos del profesor con id 1
