-- Active: 1736532502233@@127.0.0.1@3306@datag3

-- SELECT
SELECT * from empleado;
SELECT nombre,pais from empleado;
SELECT * from empleado limit 10;
SELECT * from empleado order by nombre;
SELECT * from empleado order by salario DESC;
SELECT * from empleado where pais = 'Peru';
select * from empleado where salario > 5000;
SELECT *from empleado where pais = 'Peru' and salario > 5000;