cantantes = ["2pac", 'Drake','Bad Bunny', 'Julio Iglesias']

numero =[1,2,5,8,3,4]

# ordenar
print(numero)
numero.sort()
print(numero)

# añadir elementos
cantantes.append("Natos y Waor")
cantantes.insert(1,"David Bisbal")

# Eliminar elementos
cantantes.pop(1)

# eliminar por un nombre especifico
cantantes.remove('Bad Bunny')

print(cantantes)

# dar la vuelta a la lista

print(numero)
numero.reverse()
print(numero)

# contar elementos
print(len(cantantes))

# cuantas veces aparece un elementos en la lista
print(numero.count(8))
numero.append(8)
print(numero.count(8))

# unir listas
cantantes.extend(numero)
print(cantantes)