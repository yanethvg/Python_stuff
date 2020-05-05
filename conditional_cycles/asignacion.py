calificacion = 8 #input
color = None

if calificacion >=7:
    color = 'verde'
else:
    color = 'rojo'

print(calificacion,color)
#haciendo mas pequeño el codigo
color = 'rojo'

if calificacion >=7:
    color = 'verde'

print(calificacion,color)

#haciendo mas compacto
color = 'verde' if calificacion >= 7 else 'rojo'
print(calificacion,color)