diccionario = {"a": 1, "b": 2, "c": 3, "d":4 , "e": 5, "f": 6 , "g": 7, "h": 8}

#metodos para obtener todas las llaves
resultado = diccionario.keys()
#se puede convertir a una lista o una tupla
resultado = list(resultado)
print(resultado)
"""
Salida esperada
dict_keys(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
"""
#obtener los valores del diccionario
resultado = diccionario.values()
#se puede convertir a una lista o una tupla
resultado = list(resultado)
print(resultado)
"""
Salida esperada
dict_values([1, 2, 3, 4, 5, 6, 7, 8])
"""

#obtener los valores del diccionario
resultado = diccionario.items()
#se puede convertir a una lista o una tupla, las llaves y su correspondiente valor estaran dentro de una tupla
resultado = list(resultado)
print(resultado)
"""
Salida esperada
dict_items([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5), ('f', 6), ('g', 7), ('h', 8)])
"""