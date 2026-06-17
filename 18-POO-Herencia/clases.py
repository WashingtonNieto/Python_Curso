# Herencia es la posibilidad de compartir atributos y métodos entre clases
# y que diferentes clases hereden de otros

class Persona:
    def getNombre(self):
        return self.nombre 
    
    def getApellidos(self):
        return self.apellidos 
    
    def getAltura(self):
        return self.altura 
    
    def getEdad(self):
        return self.edad 
    
    # Hasta aqui todo bien, estos métodos me permiten 
    # sacar los diferente valores que tienen esta propiedades

    # pero tambien debo tener método que me permitan ahora
    # asignarles un valor

    def setNombre(self,nombre):
        self.nombre = nombre

    def setApellidos(self,apellidos):
        self.apellidos = apellidos

    def setAltura(self,altura):
        self.altura = altura

    def setEdad(self,edad):
        self.edad = edad


    # Acciones

    def hablar(self):
        return "Estoy hablando"
    
    def caminar(self):
        return "Estoy caminando"
    
    def dorminr(self):
        return "Estoy durmiendo"
    


class Informatico(Persona):
    def __init__(self):
        self.lenguajes = "HTML, CSS, JS, PHP, Python "
        self.experiencia = 5

    def getLenguajes(self):
        return self.lenguajes
    
    def aprender(self, lenguajes):
        self.lenguajes = lenguajes
        return self.lenguajes
    
    def programar(self):
        return "Estoy programando"
    
    def reparar(self):
        return "Estoy reparando"
    

class TecnicoRedes(Informatico):
    def __init__(self):
        super().__init__() # con esto cargo en el constructor tambien la clase padre
        self.auditarRedes = 'Experto'
        self.experenciaRedes = 15

    def auditoria(self):
        return "Estoy auditando redes"