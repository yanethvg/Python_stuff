color_luz = 'rojo'
#cuatro espacios para identacion
#condiciones se van evaluando de arriba hacia abajo
#el uso del else es optativo se puede eliminar
if color_luz == 'verde':
    print('Puede continuar')
elif color_luz == 'amarillo':
    print('Alto parcial')
elif color_luz == 'rojo':
    print('Alto total')
"""
else:
    print('Alto Total')
"""
"""
valores que toma como falsos: False,"", '',[], (), {}, 0, 0.0
"""
variable = 0
if variable:
    print('Es verdadero')
else:
    print('Es falso')