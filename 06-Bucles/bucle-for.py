# Bucle for

#for variable in elementos-iterables (lista, arreglo, rango)
#   bloque de instruccion

# contador = 0
# resultado = 0

# for contador in range(0,10):
#     print(f"voy por el numero {str(contador)}")
#    #resultado = resultado + contador
#     resultado += contador

# print(f"El resultado es: {resultado}")

# print("_________Ejemplo 2______________")
# numero_usuario = int(input("Que numero de tabla de multiplicar quieres? "))
# if numero_usuario <1:
#     numero_usuario = 1

# print(f"Tabla de multiplicar {numero_usuario}")

# for numero_tabla in range(1,11):
#     print(f"{numero_usuario} x {numero_tabla} * {numero_usuario*numero_tabla}")

canasta=["mango", "naranja", "banano"]

contador = 0
for contador in range(0,10):
    for frutas in canasta:
        print(frutas)


# declaracion de ruptura
frutas = ["banano","pera", "manzana"]
for x in frutas:
    print(x)
    if x == "banano":
        break


# declaracion de continuacion
frutas = ["banano","pera", "manzana"]
for x in frutas:
    if x == "banano":
        continue
    print(x)
