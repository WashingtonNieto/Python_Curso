# Ejercicio 1
print("### Ejercicio 1 ###")
print("### Tablas de multiplicar ###")

def tabla(numero):
    print(f"Tabla de multiplicar del numero: {numero}")

    for contador in range(11):
        operacion = numero * contador
        print(f"{numero} x {contador} = {operacion}")

    print("\n")


tabla(3)
tabla(7)
tabla(12)

# Ejercicio 1.1

print("__________Todas las tablas____________________")
for numero_tabla in range(1,11):
    tabla(numero_tabla)
