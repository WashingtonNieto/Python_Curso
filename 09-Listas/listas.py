"""
Las Listas (arrays)
Son colecciones o conjuntos de datos/valores, bajo un mismo nombre.
para acceder a esos valores podemos usar un indice numerico

"""

# Definir una lista
# forma 1
peliculas = ["Batman", "Spiderman","El señor de los anillos"]

# forma 2
cantantes = list(('2pac','Drake','Michael'))

# forma 3
year = list(range(2020,2050))

# forma 4
variada = ["Mariana", 30, 4.4, True, "Texto"]


print(peliculas)
print(cantantes)
print(year)
print(variada)


# Indices
print(peliculas[1])
print(cantantes[0:2])
print(peliculas[1:])

# Modificar indices
peliculas[1] = "La Guerra de la galaxias"

# Agregar elementos a una lista
cantantes.append("Madison Bear")
# tiny, feid, Kase O, Natos y Waor

print(cantantes)

# recorrer una lista
print("\n________ Listado de peliculas___________")
for pelicula in peliculas:
    print(f"{peliculas.index(pelicula)+1}.{pelicula}")


# Añadir peliculas hasta "parar"
nueva_pelicula = ""
while nueva_pelicula != "parar":
    nueva_pelicula = input("Introduce la nueva pelicula: ")

    if nueva_pelicula != "parar":
        peliculas.append(nueva_pelicula)

print("\n________ Listado de peliculas___________")
for pelicula in peliculas:
    print(f"{peliculas.index(pelicula)+1}.{pelicula}")