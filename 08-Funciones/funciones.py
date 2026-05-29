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

# print("## Ejemplo 2 ##")
# print("## Parametros ##")
# # def mostrarNombre():
# #     print("Tu nombre es: Washington Nieto")

# # mostrarNombre()

# # def mostrarNombre(nombre):
# #     print(f"Tu nombre es: {nombre}")

# # mostrarNombre("Washington")

# # def mostrarNombre():
# #     print("Tu nombre es: Washington Nieto")

# # nombre = input("Introduce tu nombre: ")
# # mostrarNombre(nombre)

# def mostrarNombre(nombre, edad):
#     print(f"Tu nombre es: {nombre}")

#     if edad >= 18:
#         print("y eres mayor de edad!")



# nombre = input("Introduce tu nombre: ")
# edad = int(input("Introduce tu edad: "))

# mostrarNombre(nombre,edad)

# def my_function():
#   print("Hello from a function")

# my_function()
# my_function()
# my_function()

# temp1 = 77
# celsius1 = (temp1 - 32) * 5 / 9
# print(celsius1)

# temp2 = 95
# celsius2 = (temp2 - 32) * 5 / 9
# print(celsius2)

# temp3 = 50
# celsius3 = (temp3 - 32) * 5 / 9
# print(celsius3)

nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))


# def fahrenheit_to_celsius(fahrenheit):
#   return (fahrenheit - 32) * 5 / 9

# print(fahrenheit_to_celsius(77))
# print(fahrenheit_to_celsius(95))
# print(fahrenheit_to_celsius(50))

# def get_greeting():
#   return "Hello from a function"

# message = get_greeting()
# print(message)


# def my_function(animal, name):
#   print("I have a", animal)
#   print("My", animal + "'s name is", name)

# my_function(name = "Buddy", animal = "dog")



# def my_function():
#   return ["apple", "banana", "cherry"]

# fruits = my_function()
# print(fruits[0])
# print(fruits[1])
# print(fruits[2])

# def my_function(*args):
#   print("Type:", type(args))
#   print("First argument:", args[0])
#   print("Second argument:", args[1])
#   print("All arguments:", args)

# my_function("Emil", "Tobias", "Linus")

# # Ejemplo
# # Una función que calcula la suma de cualquier número de valores:
# def my_function(*numbers):
#   total = 0
#   for num in numbers:
#     total += num
#   return total

# print(my_function(1, 2, 3))
# print(my_function(10, 20, 30, 40))
# print(my_function(5))

# print(my_function(5,2,3))

# # Ejemplo
# # Hallar el valor máximo:

# def my_function(*numbers):
#   if len(numbers) == 0:
#     return None
#   max_num = numbers[0]
#   for num in numbers:
#     if num > max_num:
#       max_num = num
#   return max_num

# print(my_function(3, 7, 2, 9, 1))


# # EjemploObtén tu propio servidor Python
# # Un decorador básico que convierte a mayúsculas el valor de retorno de la función decorada.

# def changecase(func):
#   def myinner():
#     return func().upper()
#   return myinner

# @changecase
# def myfunction():
#   return "Hello Sally"

# print(myfunction())

# # Al colocarlo @changecasedirectamente encima de la definición de la función, la función myfunctionse está "decorando" con la changecase función.

# # La función changecasees el decorador.

# # La función myfunctiones la función que se decora.


# Ejemplo
# Utilizar el @changecasedecorador en dos funciones:
def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"

@changecase
def otherfunction():
  return "I am speed!"

print(myfunction())
print(otherfunction())