"""
Cómo mencionamos anteriormente, una vez que nosotros definimos una función, podemos llamarla n cantidad de veces, inclusive, fuera de nuestro script, cómo lo veremos más adelante (módulos y paquetes) es por ello que una muy buena practica de programación es documentar nuestras funciones.

Para que nosotros podamos documentar una función lo haremos mediante un comentario, comentario, el cual debe de encontrarse dentro de la función y utilizando triples comillas dobles, cómo podemos observar en el siguiente ejemplo.
"""
def mi_funcion(*args):
  """Esta es la documentación de mi_función"""
  print(args)

#Recordemos que al utilizar triples comillas dobles podemos colocar un comentario con saltos de línea.

"""
Podemos trabajar con la documentación a través de su atributo ____doc____
"""
# atributo __doc__ con punto despues de la funcion
print(mi_funcion.__doc__)