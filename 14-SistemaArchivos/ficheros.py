from io import open
import pathlib

#abrir un archivo
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
archivo = open(ruta,"a+")

# escribir
archivo.write("************ soy un texto dentro de python*********\n")

# Cerrar archivo
archivo.close()

# Abrir archivo
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
archivo_lectura = open(ruta,"r")


# # leer archivo
# contenido = archivo_lectura.read
# print(contenido)

# leer contenido y guardar en lista
lista = archivo_lectura.readlines()
archivo_lectura.close()

# una forma
print(lista)

# otra forma
for frase in lista:
    print("- "+frase)

