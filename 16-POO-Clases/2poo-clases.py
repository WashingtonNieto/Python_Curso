# programacion orientada a objetos
# (Carro)

class Coche:
    # Atributos o propiedades (variables)
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Testarossa"
    # Luce,spider,Purosangue,Amalfi,Daytona sp3,Monza SP1
    # marca = "Lamborghini"
    # modelo = "Revuelto", "Urus","Huracan","Temerario"
    velocidad = 300
    caballaje = 500
    puestos = 2

    # Metodos, son acciones que hace el objeto ,coche (funciones)
    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

    def getVelocidad(self):
        return self.velocidad

# Fin definicion clase

# Crear o instanciar un objeto

carro1 = Coche()

print(carro1.marca, carro1.color)

print("Velocidad actual: ", carro1.velocidad)

carro1.acelerar()
carro1.acelerar()
carro1.acelerar()
carro1.frenar()

print("Velocidad final: ", carro1.velocidad)
