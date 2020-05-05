def centigrados_a_farhenheit(grados):
    return grados * 1.8 + 32

# asignar una funcion a una variable
funcion_variable = centigrados_a_farhenheit(20)
print(funcion_variable)

funcion_variable = centigrados_a_farhenheit
resultado = funcion_variable(32)
print(resultado)

# Funciones anonimas, solo se realiza en una sola linea de codigo ya que realizan tareas pequeñas
# si se requieren mas de un parametro se separan por coma
# no se usa la palabra reservada return
# solo retornan un solo resultado
my_funcion = lambda grados=0 : grados * 1.8 + 32

resultado_lam = my_funcion(32)
print(resultado)

sin_parametros = lambda : True
resultado_sin = sin_parametros()
print(resultado_sin)

con_asterisco = lambda *args : args[0]
resultado_aste = con_asterisco(10,20)
print(resultado_aste)

"""
Estas son algunas formas en las cuales podemos crear funciones lambdas más complejas

sin_parametros = lambda : True

con_valores = lambda val, val1=10, val2=10 : val + val1 + val2

con_asterisco = lambda *args : args[0]

con_doble_asterisco = lambda **kwargs : args[0]

con_asteriscos = lambda *args , **kwargs : kwargs.get('key', False)
"""


