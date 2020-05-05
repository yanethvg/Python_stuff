# la variable se encuentra declarada fuera de una función son globales
# pueden usar utilizadas dentro de funciones
animal = 'Leon'

def mostrar_animal():
    print(animal)

mostrar_animal()
print(animal)

# modificando su valor dentro de una funcion
# cada vez que definimos una funcion esta define su namespace
# lugar donde se pueden definir las variables
# son variables diferentes aunque se llamen igual 
# la global es accedida por todo el script
# las variables locales solo dentro de la funcion
def mostrar_animal_dos():
    animal = 'Pinguino'
    print(animal)

mostrar_animal_dos()
print(animal)

# usando la palabra reservada global
# para modificar la variable global dentro de una funcion se utiliza la palabra reservada global
# se eliminar tambien
def mostrar_animal_tres():
    global animal
    animal = 'Pinguino'
    print(animal)

mostrar_animal_tres()
print(animal)