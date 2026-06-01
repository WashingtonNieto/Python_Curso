# Ejercicio 6
# Funciones Lambda

# Es una funcion anonima, una funcion que no tiene nombre
# y que no hace falta definirla con el def
# sirven para tareas simples, pequeñas pero que pueden llegar a ser repetitivas
# y que toda su ejecucion se limita a una linea de codigo

print("\n ### Ejemplo 6 ###")
dime_el_year = lambda year: f"El año es {year}"

print(dime_el_year(2034))