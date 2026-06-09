from io import open
import pathlib

#abrir un archivo
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
archivo = open(ruta,"a+")

# escribir
archivo.write("************ soy un texto dentro de python*********\n")