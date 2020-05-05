#mostrar en pantalla la materia con mejor promedio.

calificaciones = {'calculo':9,'dibujo':5, 'matematica':7}

keys = calificaciones.keys()

mayor = 0
for key in keys:
    if calificaciones[key] > mayor:
        mayor = calificaciones[key]


print("La nota mayor es : ",mayor)