texto = "curso de Python 3"
#pasa las primeras letras despues de un espacio a mayuscula
resultado = texto.capitalize()
print(resultado)
"""
Salida esperada
Curso de python 3
"""
#pasa las letras en minuscula a mayuscula y las mayusculas a minusculas
resultado = texto.swapcase()
print(resultado)
"""
Salida esperada
CURSO DE pYTHON 3
"""

#pasa las letras a mayusculas
resultado = texto.upper()
print(resultado)
"""
Salida esperada
CURSO DE PYTHON 3
"""


#pasa las letras a minusculas
resultado = texto.lower()
print(resultado)
"""
Salida esperada
curso de python 3
"""

#para conocer si una cadena texto viene en mayuscula
print(resultado.isupper())
"""
Salida esperada
False
"""

#para conocer si una cadena texto viene en minuscula
print(resultado.islower())
"""
Salida esperada
True
"""

#crear un formato de string con formato de titulo
resultado = texto.title()
print(resultado)
"""
Salida esperada
Curso De Python 3
"""

texto_reemplazo = "curso de Python 3,Python Basico"
#reemplaza un texto por otro
resultado = texto_reemplazo.replace("Python","Ruby")
print(resultado)
"""
Salida esperada
curso de Ruby 3,Ruby Basico
"""

#reemplaza un texto por otro, especificando la cantidad de veces a reemplazar
resultado = texto_reemplazo.replace("Python","Ruby",1)
print(resultado)
"""
Salida esperada
curso de Ruby 3,Python Basico
"""

texto_strip = "      curso de Python 3,Python Basico    "
#quita los espacios al inicio y al final
resultado = texto_strip.strip()
print(resultado)
"""
Salida esperada
curso de Python 3,Python Basico
"""
