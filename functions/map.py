"""
En Python, la función map nos permite aplicar una función sobre los items de un objeto iterable (lista, tupla, etc...).

Sintaxis
map(function, objeto iterable)
"""

#La función retornará un objeto map que posteriormente podemos convertir a una lista o tupla.
def cuadrado(numero):
    return numero * numero

lista = [1,2,3,4,5]
resultado = map(cuadrado, lista)
# le pasa la funcion y la lista y hace la operacion por cada elemento de la lista
lista_resultado = list(resultado)
print(lista_resultado)

# Es posible utilizar map junto con una función lambda. En lo personal considero esta la mejor opción.

lista_dos = [1,2,3,4,5]
resultado_dos = map(lambda numero: numero * numero , lista)

lista_resultado_dos = list(resultado_dos)
print(lista_resultado_dos)
