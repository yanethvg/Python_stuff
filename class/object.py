# crear una clase
# en ambos casos heredan de la clase object
# las funciones de dos guiones bajos son de object
# el metodo init no es el contructor de la clase
class Gato:
    def __init__(self,nombre):
        self.nombre = nombre
    # se reescribe para que no se vea el espacio en memoria
    def __str__(self):
        return self.nombre

#segunda forma de crear clases
class Pato(object):
    def __init__(self,nombre):
        self.nombre = nombre
    # se reescribe para que no se vea el espacio en memoria
    def __str__(self):
        return self.nombre


gato = Gato("bigotes")
gato.edad = 6
pato = Pato("lucas")

print(gato)
print(pato)
print("\n")
#para ver los atributos de cada clase se usa dict
print(gato.__dict__)
print(pato.__dict__)
"""
salida
{'nombre': 'bigotes', 'edad': 6}
{'nombre': 'lucas'}
"""