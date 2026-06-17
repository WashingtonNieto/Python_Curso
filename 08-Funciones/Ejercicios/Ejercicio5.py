# Ejercicio 2
print("### Ejercicio 2 ###")
print("### Parametro opcionales ###")

def getEmpleado(nombre,identificacion):
    print("Empleado")
    print(f"Nombre: {nombre}")
    print(f"Identificacion: {identificacion}")

getEmpleado("Juan Perez", "34234")


# pero si no envio el parametro saca error
# para eso utilizo el parametro opcional

# def getEmpleado(nombre,identificacion = "42342"):
def getEmpleado(nombre,identificacion = None):
    print("Empleado")
    print(f"Nombre: {nombre}")
    print(f"Identificacion: {identificacion}")

    if identificacion != None:
        print(f"Identificacion: {identificacion}")

getEmpleado("Juan Perez")