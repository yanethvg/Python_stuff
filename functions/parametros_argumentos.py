#colocando valores por default cuando no viene el parametro
def crear_usuario(nombre='',apellido='',edad=10):
    return{
        'nombre': nombre,
        'apellido': apellido,
        'nombre_completo': "{} {}".format(nombre,apellido),
        'edad': edad
    }
#se puede omitir el parametro de edad
codi = crear_usuario("Yaneth","yaneth94",25)

print(codi["nombre"])
print(codi["apellido"])
print(codi["edad"])
"""
reglas a seguir
1. No se puede asignar un valor con espacios evitar los espacios asi edad=10
2. asignacion de valores de izquierda a derecha
"""