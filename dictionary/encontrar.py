diccionario = {"a": 1, "b": 2, "c": 3, "a":4 }
#para saber si una llave existe en un diccionario
#se puede utilizar la palabra reservada in
resultado = "z" in diccionario
print(resultado)
"""
Salida esperada
False
"""
resultado = "a" in diccionario
print(resultado)
"""
Salida esperada
True
"""

#evitar el error de no encontrar la llave haciendo uso del metodo get
resultado = diccionario.get("z")
print(resultado)
"""
Salida esperada
None
"""
resultado = diccionario.get("a")
print(resultado)
"""
Salida esperada
4
"""
#se le puede asignar un segundo valor, y este se aplicara cuando la llave no exista
resultado = diccionario.get("z", "La llave no existe")
print(resultado)
"""
Salida esperada
La llave no existe
"""

#metodo setdefault si la llave existe retornara su valor
#en caso no exista la llave se genera una nueva llave clave valor y el segundo el valor
resultado = diccionario.setdefault("y", ())
print(resultado)
print(diccionario)
"""
Salida esperada
{}
"""
