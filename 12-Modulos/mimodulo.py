def holaMundo(nombre):
    return f"Hola que tal, {nombre}"


def calculadora(numero1, numero2):
    suma = numero1 + numero2
    resta = numero1 - numero2
    multiplicacion = numero1 * numero2
    division = numero1 / numero2

    cadena = ""

    cadena += "Suma: " + str(suma)
    cadena += "\n"
    cadena += "Resta: " + str(resta)
    cadena += "\n"
    cadena += "Multiplicacion: " + str(multiplicacion)
    
    return cadena