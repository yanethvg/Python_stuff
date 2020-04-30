curso = "Python"
version = "3"
#sirve para colocar los valores por reemplazo con respecto a su posición
resultado = "Curso de %s %s " %(curso,version)

print(resultado)
#haciendo uso de format
resultado = "Curso de {} {} ".format(curso,version)

print(resultado)

#haciendo uso de format, se puede nombrar a las variables dentro
#se hara con respecto al nombre no la posicion
resultado = "Curso de {a} {b} ".format(a=curso,b=version)

print(resultado)

"""
Salida esperada
Curso de Python 3
"""