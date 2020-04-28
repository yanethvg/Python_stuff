lenguajes = "Python; Javas; Ruby; PHP; Swift; JavaScript; C#; C; C++"
#metodo join se puede generar un string a partir de una lista
#se puede ser mas especifico
separador = "; "
resultado = lenguajes.split(separador)
print(resultado)
"""
Salida esperada
['Python', 'Javas', 'Ruby', 'PHP', 'Swift', 'JavaScript', 'C#', 'C', 'C++']
"""
#se va a generar un string con esta lista
nuevo_string= " ".join(resultado)
# se coloca el espacio porque separara cada elemento de la lista con ese espacio
print(nuevo_string)
"""
Salida esperada
Python Javas Ruby PHP Swift JavaScript C# C C++
"""
nuevo_string= "_".join(resultado)
#para que se separen con un _ guion bajo
print(nuevo_string)
"""
Salida esperada
Python_Javas_Ruby_PHP_Swift_JavaScript_C#_C_C++
"""

nuevo_string= " Curso: ".join(resultado)
#se puede colocar una palabra
print(nuevo_string)
"""
Salida esperada
Python Curso: Javas Curso: Ruby Curso: PHP Curso: Swift Curso: JavaScript Curso: C# Curso: C Curso: C++
"""

#para regresarlo a como estaba antes
nuevo_string= separador.join(resultado)
print(nuevo_string)
"""
Salida esperada
Python; Javas; Ruby; PHP; Swift; JavaScript; C#; C; C++
"""