# el constructor es un método especial dentro de una clase
# que se suele utilizar para darle un valor  a los atributos del objeto
# al crearlo
# es decir... es el primer metodo que se ejecuta al crear el objeto
# y se llama automáticamente al crearlo


class Coche:

    # # visibilidad
    # soy_publico = "Hola, soy un atributo público"
    # __soy_privado = "hOLA, SOY UN atributo privado"

    # def getPrivato(self):
    #     return self.__soy_privado

    # Atributos o propiedades (variables)
    def __init__(self, color, marca, modelo, velocidad, caballaje, puestos):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje = caballaje
        self.puestos = puestos




    # Metodos, son acciones que hace el objeto ,coche (funciones)
    # la mejor manera es hacerlo con get y set, por ejemplo para modificar el color de una propiedad
    # simplemente debo pasar un par de argumentos al metodo
    # primero el self y el color que voy asignarle realmente a la propiedad color
    def setColor(self, color):
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


    # se puede generar un metodo que me genere todos
    # los metodos de golpe
    def getInfo(self):
        info = "---- información del carro------"
        info += "\n Color: " + self.getColor()
        info += "\n Marca: " + self.getMarca()
        info += "\n Modelo: " + self.getModelo()
        info += "\n Velocidad: " + str(self.getVelocidad())

        return info
# Fin definicion clase
