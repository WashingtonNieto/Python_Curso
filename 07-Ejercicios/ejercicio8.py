# Ejercicio 8. Sacar el porcentaje de un numero
# ambos numeros pedido al usuario

numero = int(input("Introduce el número: "))
porcentaje = int(input(f"Qué porcentaje quieres sacar al {numero}?"))

operacion = (numero * (porcentaje/100))

print(f"El {porcentaje}% de {numero} es: {operacion}")