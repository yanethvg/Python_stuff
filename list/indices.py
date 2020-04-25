cursos = ["python", "django", "flask","c","c++","c#","java","php"]

# se puede acceder de derecha a izquierda
curso = cursos[-1]
#se puede acceder de izquierda a derecha
curso = cursos[1]

#se puede generar una sublita de una lista
sub = cursos[0:3]
#se puede omitir el comienzo
sub = cursos[:3]
#se puede omitir el final
sub = cursos[5:]
#se puede poner la cantidad de saltos que se quiere es el tercer parametro
sub = cursos[1:7:2]
#indicando el reverso de los elementos inverso de la lista
sub = cursos[::-1]
print(sub)