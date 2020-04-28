lenguajes = "Python; Javas; Ruby; PHP; Swift; JavaScript; C#; C; C++"
#metodo split
resultado = lenguajes.split()
#hace una nueva lista a partir del texto utilizado dividido por defector por espacio
print(resultado)
"""
Salida esperada
['Python;', 'Javas;', 'Ruby;', 'PHP;', 'Swift;', 'JavaScript;', 'C#;', 'C;', 'C++']
"""
#si no se quiere que se divida por espacios como por defecto
#se ingresa el string por el cual se va a dividir
resultado = lenguajes.split(";")
print(resultado)
"""
Salida esperada
['Python', ' Javas', ' Ruby', ' PHP', ' Swift', ' JavaScript', ' C#', ' C', ' C++']
"""
#se puede ser mas especifico
separador = "; "
resultado = lenguajes.split(separador)
print(resultado)
"""
Salida esperada
['Python', 'Javas', 'Ruby', 'PHP', 'Swift', 'JavaScript', 'C#', 'C', 'C++']
"""