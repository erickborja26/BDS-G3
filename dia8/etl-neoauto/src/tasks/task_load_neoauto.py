import mysql.connector
from prefect import task

@task(name="Cargar data en base de datos")
def task_load_neoauto(autos):
    
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="datag3")
        cursor = connection.cursor()
        
        query_table = """CREATE TABLE IF NOT EXISTS autos(
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(255),
            url VARCHAR(255),
            precio DOUBLE)"""
        cursor.execute(query_table)
        connection.commit()
        
        query_insert = """INSERT INTO autos(nombre, url, precio) VALUES (%s, %s, %s)"""
        
        for auto in autos:
            cursor.execute(query_insert, (auto['nombre'], auto['url'], auto['precio']))
        
        connection.commit()
        cursor.close()
        connection.close()
        print("Data cargada en base de datos")
    
    except mysql.connector.Error as e:
        print("Error al cargar data en base de datos: {}".format(e))