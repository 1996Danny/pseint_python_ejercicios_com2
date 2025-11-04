create schema empresa_db;
use empresa_db;

create table oficinas(
	id int primary key auto_increment not null,
    nombre varchar(50) not null,
    ciudad varchar(100) not null
);

create table empleados(
	id int primary key auto_increment not null,
    nombre varchar(50) not null,
    apellido varchar(50) not null,
    salario float,
    cargo varchar(50),
    telefono varchar(50),
    correo varchar(100) unique,
    fecha_nacimiento date,
    id_oficina int,
    foreign key (id_oficina) references oficinas(id)
);

insert into oficinas(id, nombre, ciudad) 
values (1, 'Oficina Central', 'Resistencia');

insert into oficinas(id, nombre, ciudad) 
values (2, 'Oficina Sur', 'Corrientes'),
		(3, 'Oficina Norte', 'Cordoba'),
        (4, 'Oficina Este', 'Resistencia');

select * from oficinas;

insert into empleados(
	id, nombre, apellido, salario, 
    cargo, telefono, correo, fecha_nacimiento, id_oficina) 
values(
    1, 'Juan', 'Marquez', 1500, 'gerente de ventas',
    '123445', 'juan@gmail.com', '1990-10-25', 3);
    
insert into empleados(
	id, nombre, apellido, salario, 
    cargo, telefono, correo, fecha_nacimiento, id_oficina) 
values(
    2, 'Pedro', 'Sanchez', 1000, 'secretario',
    '54674567', 'pedro@gmail.com', '1998-1-7', 1),
    (3, 'Maria', 'Soler', 1400, 'marketing',
    '6796789', 'maria@gmail.com', '2000-11-3', 1),
    (4, 'Rosana', 'Rodriguez', 2000, 'Director desarrollo',
    '56745667', 'Rosana@gmail.com', '1980-5-20', 4);
    
select * from empleados;
select nombre, apellido, salario from empleados order by salario;

select avg(salario) as promedio_salario from empleados;

-- nombre apellido de loe empledos que estan en una oficina

select e.nombre, e.apellido from empleados e
inner join oficinas o on o.ciudad = 'Resistencia';

select e.nombre, e.apellido, o.ciudad from empleados e
right join oficinas o on o.ciudad = 'Resistencia';


select nombre, apellido, salario 
from empleados 
where salario < (select avg(salario) from empleados);

start transaction;

update empleados set salario = 5000 where id = 1;
update empleados set cargo = "director marketing" where id = 1;
select * from empleados;

rollback; commit;