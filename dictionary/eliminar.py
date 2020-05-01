diccionario = {"a": 1, "b": 2, "c": 3, "d":4 , "e": 5, "f": 6 , "g": 7, "h": 8}

#eliminar un valor por medio de su key
del diccionario["a"]
#otra forma es utilizando el metodo pop retorna el valor
valor = diccionario.pop("b")
#para eliminar todos los valores del diccionario
diccionario = {}
#otra forma de eliminar todos los valores es utilizando el metodo clear
diccionario.clear()

print(valor)
print(len(diccionario))
print(diccionario)

