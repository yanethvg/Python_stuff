# primera forma de importacion
# import calculadora
# usando la palabra reservada from 
"""
Cuando nos encontremos trabajando con módulos, es una buena práctica de programación que nosotros documentamos estos, más aún, cuando pensamos en liberarlos.

Para documentar un módulo requerimos trabajar con comentarios
"""
#from calculadora import *
"""
from calculadora import (resta,
                        suma,
                        division
                        )
"""
# se puede renombrar al objeto importado
from calculadora import (resta as res,
                        suma as sumita,
                        division as div
                        )
#mandando a llamar el modulo documentado
#import documentacion_modulos
#help(documentacion_modulos)
#resultado = calculadora.resta(10,5)
resultado = res(10,5)
print(resultado)

#resultado = calculadora.suma(10,5)
resultado = sumita(10,5)
print(resultado)

resultado = div(10,5)
print(resultado)



