diccionario = {}
#asignando la primera llave y valor
diccionario["nombre"] = "Codi" #Para agregar una llave con su valor
print(diccionario)
"""
Salida esperada
{'nombre': 'Codi'}
"""

#obteniendo el valor por medio de su llave
valor = diccionario["nombre"]
print(valor)
"""
Salida esperada
Codi
"""

#modificando su valor
#si la llave no existe se crea la llave y se almacena el valor
diccionario["nombre"] =  90
print(diccionario)
"""
Salida esperada
{'nombre': 90}
"""
#se queda con el ultimo valor asignado
#no pueden existir llaves duplicadas
diccionario_dos = {"a": 1, "b": 2, "c": 3, "a":4 }
print(diccionario_dos)

