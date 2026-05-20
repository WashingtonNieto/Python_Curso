print("Hola mundo")

# comentarios"

# variables
texto = "Python para principiantes"
nombre = "Washington Nieto"
year = 2019

print(texto)
print(nombre)
print(year)

# concatenar
print(texto +"-"+ nombre +"-"+ str(year))
print(f"{texto}-{nombre}-{str(year)}")

# entrada de datos
añoDeNacimiento = int(input("Cual es tu año de nacimiento?: "))
print(añoDeNacimiento)

# condicionales
if añoDeNacimiento > 2008:
    print("Eres un adolescente")
else:
    print("Eres un adulto")