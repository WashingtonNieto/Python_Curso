from coche import Coche

carro1 = Coche("Amarillo","Renault","Clio",150,200,4)
carro2 = Coche("Verde","Seat","Panda",240,500,4)
carro3 = Coche("Azul","Citroen","Xara",300,180,4)
carro4 = Coche("Rojo","Mercedes","Clase A",350,480,4)


# print(carro1.getColor())
# print(carro1.getMarca())
# print(carro1.getModelo())

print(carro1.getInfo())
print(carro2.getInfo())
print(carro3.getInfo())
print(carro4.getInfo())

# detectar el tipado de un dato
# por ejemplo quiero saber si un dato es de tipo objeto
# para tomar alguna decisión

# carro3 = "cualquier datos"
if type(carro3) == Coche:
    print("Es un objeto correcto!")
else:
    print("Ojo, No es un objeto!")

print(carro1.soy_publico)