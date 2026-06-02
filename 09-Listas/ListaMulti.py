# Listas multidimensionales

print("\n ***** Listado de contactos *****")
contactos=[
    [
        'Katerin',
        'antonio@gmail.com'

    ],
    [
        'Luis',
        'luis@gmail.com'

    ],
    [
        'Maria',
        'maria@gmail.com'

    ],
    [
        'Salvador',
        'salvador@gmail.com'

    ]

]

print(contactos)

print(contactos[1])
print(contactos[1][1])

for contacto in contactos:
    print(contacto[0])


for contacto in contactos:
    for elemento in contacto:
        print(elemento)
    print("\n")