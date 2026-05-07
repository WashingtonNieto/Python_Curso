print("Hola mundo")

# comentarios

# Variables
texto = "Python para principiantes"
nombre = "washington Nieto"
year=2019

print(texto)
print(nombre)
print(year)

# concatenar
print(f"{texto}-{nombre}-{str(year)}")
print(texto +" - "+nombre +" - "+str(year))

# entrada de datos
# sitioweb = input("¿cual es tu pagina web: ")
# print(sitioweb)

# condiciones
anioDeNacimiento = int(input("Cual es tu año de nacimiento?: "))
if anioDeNacimiento >=2010:
    print("Eres un adolescente")
else:
    print("Eres un adulto")

# funciones
var_anioDeNacimiento = int(input("Cual es tu año de nacimiento?: "))

def mostarEdad(anioDeNacimiento):
    
    if anioDeNacimiento >=2010:
        print("Eres un adolescente")
    else:
        print("Eres un adulto")
    
    

mostarEdad(var_anioDeNacimiento)
mostarEdad(var_anioDeNacimiento)
mostarEdad(var_anioDeNacimiento)

"""
def mostarEdad(anioDeNacimiento1):
    resultado =""
    
    if anioDeNacimiento >=2010:
       resultado = "Eres un adolescente"
    else:
        resultado = "Eres un adulto"
    return

print(mostarEdad(var_anioDeNacimiento))

"""
# Listas
personas = ["Maria","Paco","jose"]
print(personas)
print(personas[1])

# mostrar todos los integrandtes de la lista
for persona in personas:
    print("-"+persona)

