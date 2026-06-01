nombre = input("Entre su nombre: ")
edad = int(input("entre su edad: "))
colombia = input("Es usted colombiano s/n ?")
 
while colombia == "s" and edad >=18:
    print("Usted esta habilitado para vota")  
else:
    print("Usted NO esta habilitado para vota")  