"""
Mostrar en pantalla la frecuencia de aparición de vocales en una frase dada por el usuario.
"""

frase = input("Ingresa tu mensaje: ")

vocales = "AEIOUaeiou"
count = 0
# Busqueda de vocales en la frase.
for vocal in frase:
    # Si la vocal esta en la frase 
    # la sumas a el total.
    if vocal in vocales:
        count += 1

print(f"\tSon {count} las vocales que contiene el mensaje.")