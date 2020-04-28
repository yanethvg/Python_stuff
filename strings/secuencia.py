curso = "Curso de Python 3"

cantidad = len(curso)

resultado = curso[0]
resultado = curso[-1]

#se puede generar substring
resultado = curso[1:16:2]

print(resultado)

#modificar un valor en el string
#igual que las tuplas los string son inmutables curso[0] = "E"

print(curso)