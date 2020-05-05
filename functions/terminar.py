# una funcion terminara hasta que la ultima linea de codigo sea ejecutada dentro de la función
def mi_funcion():
    print("Un mensaje")
    print("Un mensaje dos")
    return 2
    
#el mensaje dos no se visualizara 
# la función terminara con la palabra reservada return

resultado = mi_funcion()
print(resultado)
"""
Salida esperada None
"""

def mi_funcion_dos(parametro):
    if parametro:
        return 100
    
resultado = mi_funcion_dos("")
if resultado:
    print("El resultado no es None")
"""
Salida esperada None
"""
#cuando se ejecute la ultima linea de codigo
#cuando se ejecute la linea return