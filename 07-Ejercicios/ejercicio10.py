# Ejercicio 10
# pedir la nota a unos alumnos
# y sacar por pantalla cuantos han aprobado y cuantos no

contador = 1
aprobados = 0
reprobados = 0

numero_alumnos = int(input("cuantos alumnos tienes? "))

while contador <= numero_alumnos:
    nota = int(input(f"Que nota tiene el alumno {contador}? "))
    if nota >= 5:
        aprobados +=1
    else:
        reprobados +=1

    contador += 1

print(f"Alumnos aprobados: {aprobados}")
print(f"Alumnos reprobados: {reprobados}")

