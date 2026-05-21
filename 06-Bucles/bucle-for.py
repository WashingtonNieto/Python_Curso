# Bucle for se utiliza para iterar sobre una secuencia
# que puede ser una lista, una tupla o un diccionario
# o un conjunto

# Esto se parece menos a la palabra clave "for" en otros lenguajes
# y funciona mas como un iterador.

# con el bucle for podemos ejecutar un conjunto de instruccion a 
# medido que el ciclo itera 

# print("### Ejemplo 1 ###")
# contador = 0
# for contador in range(0, 10):
#     print(f"Voy por el valor {contador}")
# else:
#     print("Fin del programa")

# print("### Ejemplo 2 ###")
# print("### Nomina ###")
# nomina = ["Pedro","Ramiro","Luz","Marta"]

# for empleados in nomina:
#     print(f"El sueldo de {empleados} es de $2millones")
# else:
#     print("Fin del programa")

# print("### Ejemplo 3 ###")
# print("### Canasta ###")
# canasta = ["Mango","Pera","Manzana","Melocoton","Fresa"]

# for fruta in canasta:
#     print(f"{fruta} esta en la canasta")
# else:
#     print("Fin del programa")

print("### Ejemplo 4 ###")
print("### Par/impar ###")

for contador in range(0,100):
    if contador%2 == 0:
        print(f"{contador} es par")
    else:
        print(f"{contador} es impar")
else:
    print("fin del programa")