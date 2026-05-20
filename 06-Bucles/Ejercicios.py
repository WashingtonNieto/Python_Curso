#print("Ejercicio 1")
#crear tres variables
#pais
#continente
#año
# imprimir la variable y frente su tipo de dato


#print("ejercicio 2")
#Todos los numeros pares del 1 al 120
# for contador in range(1,121):
#     if contador%2==0:
#         print(f"{contador} es par")
#     else:
#         print(f"{contador} no es par")


# print("ejercicio 3")
# Imprimir los cuadrados (numero multiplicado por si mismo)
# de los primeros 60 numeros.
# resolver con for y con while

# while
# contador = 0
# while contador <= 60:
#     cuadrado = contador * contador
#     print(f"El cuadrado de {contador} es {cuadrado}")
#     contador += 1
# else:
#     print("Fin del programa")

# for
# for numero in range(61):
#     cuadrado = numero * numero
#     print(f"El cuadrado de {numero} es {cuadrado}")
# else:
#     print("Fin del programa")

#print("ejercicio 4")
# Hacer un programa que muestre todos los numeros
# que hay entre dos numeros digitados por un usuario

# numero1 = int(input("Introduce el primer numero: "))
# numero2 = int(input("Introduce el segundo numero: "))

# if numero1 < numero2:
#     for contador in range(numero1,(numero2+1)):
#         print(contador)
# else:
#     print("El numero 1 debe ser  menor al numero 2")



# print("ejercicio 5")

# Mostrar todas las tablas de multiplicar del 1 al 10
# mostrando el titulo de la tabla y las multiplicaciones
for cabecera in range(1,11):
    print("##################")
    print(f"## Tabla del {cabecera} ##")
    print("##################")

    for numero in range(1,11):
        print(f"{numero} x {cabecera} = {numero*cabecera}")
    
    print("\n")