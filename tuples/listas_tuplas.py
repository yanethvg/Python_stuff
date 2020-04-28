lista = ["Curso","Python","CodigoFacilito"]
tupla = ("Introducción","Básico","Listas","Tuplas")

#convirtiendo una tupla a una lista
nueva_lista = list(tupla)
print(nueva_lista)
"""
Salida esperada
['Introducción', 'Básico', 'Listas', 'Tuplas']
"""
#convirtiendo una lista a una tupla
nueva_tupla = tuple(lista)
print(nueva_tupla)
"""
Salida esperada
('Curso', 'Python', 'CodigoFacilito')
"""
#ninguno modifica el dato original

mensaje = "Este es un curso de Python"
#pasando a list o a tuple
nuevo_mensaje = list(mensaje)
print(nuevo_mensaje)
"""
Salida esperada
['E', 's', 't', 'e', ' ', 'e', 's', ' ', 'u', 'n', ' ', 'c', 'u', 'r', 's', 'o', ' ', 'd', 'e', ' ', 'P', 'y', 't', 'h', 'o', 'n']
"""