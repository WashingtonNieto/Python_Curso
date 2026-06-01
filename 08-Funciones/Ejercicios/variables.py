"""
Variables locales: Se definen dentro de la funcion y no se pueden usar fuera de ella,
solo están disponibles dentro.
a no ser que hagamos un return.

Variables globales: Son las que se declaran fuera de una función y estan disponibles
dentro y fuera de la función

"""

# variable global
frase = "Ni los genios son tan genios, ni los tontos son tan tontos"

print(frase)

def holaMundo():
    frase = "Hola mundo!"
    print(frase)

    year = 2021
    print(year)

    global website
    website = "microsoft.com"

    print("Dentro: ", website)

    return "dato devuelto " + str(year)

print(holaMundo())
print("Fuera: ", website)

# Conclusion: una variable local solo puede usarse dentro de la funcion
# y una variable global se puede usar desde dentro o fuera
# si yo quiero usar una variable local como una global debo: 1) hacerle return 2) declararla como global