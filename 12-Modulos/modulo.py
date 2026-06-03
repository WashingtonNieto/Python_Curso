"""
Modulo: Son funcionalidades ya creadas para re-utillizar

En python hay mucho modulos, que los puedes consultar en :
https://docs.python.org/3/library/math.html#module-math
https://docs.python.org/es/3/tutorial/modules.html

Se pueden conseguir modulos que ya vienen en el lenguaje
modulos en interner, y modulos que creamos 
"""

# # importar todo modulo propio
# import mimodulo

# print(mimodulo.holaMundo("Washington"))
# print(mimodulo.calculadora(3,5))


# # importar solo una parte
# from mimodulo import holaMundo
# print(holaMundo("Washington"))

# Importar todos los modulo con from
from mimodulo import *
print(holaMundo("Washington"))
print(calculadora(5,7))
