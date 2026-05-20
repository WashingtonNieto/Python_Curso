print("Hola Mundo")

"""
comentarios

"""

# comentarios

# variables
texto = "Python para principiantes"
nombre = "Washington Nieto"
year = 2019

print(texto)
print(nombre)
print(year)

# concatenar
print(texto +" - "+ nombre +" - "+ str(year))

print(f"{texto}-{nombre}-{str(year)}")

# entrada de datos
# sitioweb =input("Cual es su sitio web favorito?: ")

# anioDeNacimiento = int(input("cual es su año de cumpleaños? fifa"))

# condicionales
# if anioDeNacimiento <2008:
#     print("Usted es un adulto")
# else:
#     print("Usted es un niño")

# Listas
personas = ["Paco","Mariana","Teresa"]
print(personas)
print(personas[1])

# mostrar todos los elementos de la lista
for persona in personas:
    print("-"+persona)