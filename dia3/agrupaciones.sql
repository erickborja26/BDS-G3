-- Active: 1736532502233@@127.0.0.1@3306@datag3

--FUNCIONES DE AGRUPACIÓN

-- 1. contar
select count(*) from empleado;
select COUNT(*) from empleado where salario > 5000;

--maximo , minimo, promedio(average)
select max(salario), min(salario), AVG(salario) from empleado;
select DISTINCT pais from empleado;

--AGRUPAMIENTO DE PAISES CON LA CANTIDAD Q HAY
select pais, count(*) from empleado
group by pais
order by count(*) DESC;

-- salario min y max y  promedio por pais

select pais, area, min(salario), max(salario), avg(salario) from empleado
GROUP BY pais, area;

-- salarios mayores a 5000 sacar total
select pais, area, min(salario), max(salario), avg(salario) from empleado
where salario > 5000
GROUP BY pais, area;

select pais, avg(salario) from empleado
GROUP BY pais
having avg(salario) > 5000;

-- SUBCONSULTAS
SELECT avg(salario) from empleado;
SELECT * FROM empleado
WHERE salario > (SELECT avg(salario) from empleado);

SELECT pais, count(*), (SELECT AVG(salario) from empleado) as salario_promedio from empleado
where salario > (SELECT AVG(salario) from empleado)
GROUP BY pais order by count(*) desc;