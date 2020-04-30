mensaje = "Este es un texto un poco grande en cuanto a longitud de caracteres se refiere"
#funcion para buscar 
resultado = mensaje.count("e")
print(resultado)
"""
Cuantas veces aparece este texto
12
"""

#haciendo uso de la palabra reservada in
resultado = "texto" in mensaje
print(resultado)
"""
Retorna un boolean
True
"""
resultado = "texto" not in mensaje
print(resultado)
"""
Retorna un boolean
False
"""

resultado = mensaje.find("texto")
print(resultado)
"""
Retorna la posición de la primera letra del string a buscar 
11
"""
#para extraer a partir de la posición y el parametro de buscqueda
resultado = mensaje[resultado:resultado + len("texto")]
print(resultado)
"""
Salida
texto
"""

#para saber si esta al inicio de una cadena es sensible E y e retorna diferente
resultado = mensaje.startswith("Este")
print(resultado)
"""
Salida
True
"""

#para saber si esta al final de una cadena es sensible E y e retorna diferente
resultado = mensaje.endswith("e")
print(resultado)
"""
Salida
True
"""