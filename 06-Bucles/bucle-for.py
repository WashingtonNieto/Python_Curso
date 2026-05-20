# Bucle for (tomado de W3Scholl)

# Un bucle for se utiliza para iterar sobre una secuencia 
# (que puede ser una lista, una tupla, un diccionario, 
# un conjunto o una cadena de caracteres).

# Esto se parece menos a la palabra clave `for` en otros lenguajes de programación
# y funciona más como un método iterador, como los que se encuentran en otros 
# lenguajes de programación orientados a objetos.

# Con el bucle for podemos ejecutar un conjunto de instrucciones, 
# una vez por cada elemento de una lista, tupla, conjunto, etc.

# contador = 0
# for contador in range(0,10):
#     print(f"Voy por el numero {contador}")
# else:
#     print("Fin del program")


# # nomina
# nomina = ["pepa","Juan","Maria","Raul"]

# for empleados in nomina:
#     print(f"El sueldo de {empleados} es de $2 millones")
# else:
#     print("Fin de la nomina")

# # canasta
# canasta = ["Pera","Mangostino","Fresa","Melocoton","Mango"]
# for fruto in canasta:
#     print(f"{fruto} es un elemento que hay en la canasta")
# else:
#     print("se acabo la canasta")

#resultado
# contador = 0
# resultado = 0

# for contador in range(0,10):
#     print(f"voy por el numero {contador}")
#     resultado = resultado + contador
    
# else:
#     print(f"El resultado es: {resultado}")
#     print("fin del contador")

#tabla de multiplicar

# tabla = int(input("Entre la tabla que necesita: "))
# print(f"## tabla del {tabla} ##")
# for numero in range(1,11):
#     print(f"{tabla} x {numero} = {tabla * numero}")
# else:
#     print("fin de la tabla")

# declaracion de ruptura
# frutas = ["banano","pera","manzana"]
# for x in frutas:
#     print(x)
#     if x == "banano":
#         break

# declaracion de continuacion
frutas = ["Fresa","Mango","Pomarosa","Melocoton"]
for x in frutas:
    if x == "Pomarosa":
        continue
    print(x)