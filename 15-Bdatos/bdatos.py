import mysql.connector

conexion = mysql.connector.connect(
    user='root',
    password='',
    host='localhost',
    database='Bd_python', 
    port='3306')

# comprobar conexion
print(conexion)

cursor = conexion.cursor()

# # crear bdatos
# cursor.execute("CREATE DATABASE IF NOT EXISTS Bd_python")

# # Crear tablas
# cursor.execute ("""
# CREATE TABLE IF NOT EXISTS vehiculos(
# id int(10) auto_increment not null,
# marca varchar(40) not null,
# modelo varchar(40) not null,
# precio float(10,2) not null,
# CONSTRAINT pk_vehiculo PRIMARY KEY(id)
# )
# """)

# cursor.execute ("SHOW TABLES")
# for table in cursor:
#     print(table)

# # insertar datos dentro de una tabla
# cursor.execute("INSERT INTO vehiculos VALUES(null, 'BMW', 'i4', 35000)")
# conexion.commit()


# # insertar datos dentro de una tabla en forma masiva

# carros = [
#     ('Seat', 'Ibiza', 5000),
#     ('Renault', 'Clio', 7000),
#     ('Citroen','Saxo',6500),
#     ('Mercedes','Clase C', 25000)
# ]

# cursor.executemany("INSERT INTO vehiculos VALUES (null, %s, %s, %s)", carros)
# conexion.commit()