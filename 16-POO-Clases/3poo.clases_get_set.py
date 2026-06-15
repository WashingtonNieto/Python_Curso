# programacion orientada a objetos
# (Carro)

class Coche:
    # Atributos o propiedades (variables)
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Testarossa"
    # Luce,spider,Purosangue,Amalfi,Daytona sp3,Monza SP1
    # marca = "Lamborghini"
    # modelo = "Gallardo", "Aventador", "murciélago","Revuelto", "Urus","Huracan","Temerario"
    velocidad = 300
    caballaje = 500
    puestos = 2

    # Metodos, son acciones que hace el objeto ,coche (funciones)
    # la mejor manera es hacerlo con get y set, por ejemplo para modificar el color de una propiedad
    # simplemente debo pasar un par de argumentos al metodo
    # primero el self y el color que voy asignarle realmente a la propiedad color
    def setColor(self,color):
        self.color = color
        # y de esta manera estamos asignado a la propiedad self.color el colo que queremos
    
    # y para sacar el color de las propiedades hacemos lo contrario
    def getColor(self):
        return self.color #asi traemos el color
    
    def setMarca(self, marca):
        self.marca = marca
    
    def getMarca(self):
        return self.marca

    def setModelo(self, modelo):
        self.modelo = modelo
    
    def getModelo(self):
        return self.modelo
    
    
    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

    def getVelocidad(self):
        return self.velocidad

# Fin definicion clase

# Crear o instanciar un objeto

carro1 = Coche()

print ("\n______________________")
print("Carro 1")

carro1.setMarca("Ferrari")
carro1.setModelo("spider")
carro1.setColor("Amarillo")

print(carro1.getMarca(), carro1.getModelo(), carro1.getColor())

print("Velocidad actual: ", carro1.getVelocidad())

print ("\n______________________")

# creo la instancia para el carro 2
carro2 = Coche()
print("Carro 2")

carro2.setMarca("Lamborghini")
carro2.setColor("Verde")
carro2.setModelo("Gallardo")

print(carro2.getMarca(), carro2.getModelo(), carro2.getColor())
print("Velocidad actual: ", carro2.getVelocidad())

# si quiero saber que tipo de datos es carro1 por ejemplo
print(type(carro1))  # me muestra que el tipo de dato es una clase


