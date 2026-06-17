print("### Ejercicio 5 ###")
print("### Funciones dentro de una funcion ###")

def getNombre(nombre):
    texto = f"El nombre es: {nombre}"
    return texto

def getApellidos(apellidos):
    texto = f"Los apellidos son: {apellidos}"
    return texto

print(getNombre("Ricardo"), getApellidos("perez"))


def devuelveTodo(nombre,apellidos):
    texto = getNombre(nombre) + "\n" + getApellidos(apellidos)
    return texto

print(devuelveTodo("Jorge","Martinez"))

