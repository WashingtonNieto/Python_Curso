# tomado https://www.w3schools.com/python/python_functions.asp
# Una función es un bloque de código que solo se ejecuta cuando se la llama.
# Una función puede devolver datos como resultado.
# Una función ayuda a evitar la repetición de código.

# En Python, una función se define utilizando la def palabra clave, seguida del nombre de la función y paréntesis:
# def mi_funcion():
#     print("Hola esto es una funcion")

# mi_funcion()


# print("# ejemplo 1")
# #defino la funcion
# def muestraNombre():
#     print("Victor")
#     print("Paco")
#     print("Juan")
#     print("Francisco")
#     print("Angela")
#     print("Victoria")
#     print("Jorge")
#     print("\n")

# #invocar la funcion
# muestraNombre()

print("## Ejemplo 2 ##")
print("## Parametros ##")
# def mostrarNombre():
#     print("Tu nombre es: Washington Nieto")

# mostrarNombre()

# def mostrarNombre(nombre):
#     print(f"Tu nombre es: {nombre}")

# mostrarNombre("Washington")

# def mostrarNombre():
#     print("Tu nombre es: Washington Nieto")

# nombre = input("Introduce tu nombre: ")
# mostrarNombre(nombre)

def mostrarNombre(nombre, edad):
    print(f"Tu nombre es: {nombre}")

    if edad >= 18:
        print("y eres mayor de edad!")



nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))

mostrarNombre(nombre,edad)



