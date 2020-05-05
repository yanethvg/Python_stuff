"""
Eliminar todas las vocales de una frase dado por el usuario y mostrar el nuevo string en pantalla.
"""

frase = input("Ingresa tu mensaje: ")
nueva_frase = ""
vocales = "AEIOUaeiou"
count = 0
# Busqueda de vocales en la frase.
for vocal in frase:
    if vocal not in vocales:
        nueva_frase = nueva_frase + vocal

print(f"\tNueva Frase:  {nueva_frase} ")
