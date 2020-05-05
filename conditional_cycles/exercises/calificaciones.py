"""
Dado un diccionario, el cual almacena las calificaciones de un alumno, siendo las llaves los nombres de las materia y los valores las calificación, mostrar en pantalla el promedio del alumno.
Ejemplo: calificaciones = {calculo:10, dibujo:5}

"""

calificaciones = {'calculo':10,'dibujo':5, 'matematica':7}

keys = calificaciones.keys()

suma = 0
for key in keys:
    suma = suma + calificaciones[key]

promedio = suma/ len(keys)

print("El promedio es: ",promedio)