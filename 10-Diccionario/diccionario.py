"""
Diccionario:
Un tipo de dato que almacena un conjunto de datos.
En formato clave > valor
Es parecido a un array asociativo o un objeto json.

"""

persona = {
    "nombre": "Washington",
    "apellido":"nieto",
    "pais":"Colombia"
}

print(persona)

print(persona["pais"])

contactos = [
    {
        'nombre':'Antonio',
        'email': 'antonio@gmail.com'
    },
    {
        'nombre':'Luis',
        'email': 'luis@gmail.com'
    },

    {
        'nombre':'Maria',
        'email': 'maria@gmail.com'
    },

    {
        'nombre':'Pepe',
        'email': 'pepe@gmail.com'
    }
]

contactos[0]['nombre'] = "Antoñito"
print(contactos[0]['nombre'])

print("\n Listado de contactos: ")
print("_________________________________")

for contacto in contactos:
    print(f"Nombre del contacto: {contacto['nombre']}")    
    print(f"Email del contacto: {contacto['email']}")
print("_________________________________")
