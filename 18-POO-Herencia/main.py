import clases

persona = clases.Persona()
persona.setNombre("Juan")
persona.setApellidos("Perez")
persona.setAltura("170cm")
persona.setEdad("30 años")

print(f"La persona es {persona.getNombre()} {persona.getApellidos()}")
print(persona.hablar())
print("---------------------------")

informatico = clases.Informatico()
informatico.setNombre("Carlos")
informatico.setApellidos("Martinez")

print(f"El informatico es: {informatico.getNombre()} {informatico.getApellidos()}")
print(informatico.getLenguajes())
print(informatico.experiencia)
print(informatico.caminar())
print("---------------------------")

tecnico = clases.TecnicoRedes()
tecnico.setNombre("Jorge")
print(tecnico.auditarRedes,tecnico.getNombre(),tecnico.getLenguajes())