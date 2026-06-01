numero_usuario = int(input("Que numero de tabla de multiplicar quieres? "))
contador = 0
while contador <= 10:
    print(f"{numero_usuario} X {contador} = {numero_usuario*contador}")
    contador +=1 
else:
    print("Tabla terminada")