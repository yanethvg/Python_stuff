#cuando no se conoce el numero de parametros que se van a recibir
#en ese caso se puede poner un asterisco
def suma(val1,val2,val3):
    return val1 + val2 + val3

resultado = suma(10,20,30)
print(resultado)

#refactorizando
#acepta varios parametros sin problema
# el asterisco agrupara todos los elementos a una tupla y asignada a la variable
def suma_args(*args):
    total = 0
    for valor in args:
        total+=valor
    return total

resultado = suma_args(10,20,30,40,50)
print(resultado)

# el uso del asterisco, no limina el uso de otros parametros solo debe ponerse al final
# convencion el nombre del parametro debe de ser args el que se pone con asterisco
# el parametro args es una tupla
def suma_args_param(parametro_requerido,*args):
    total = 0
    print(parametro_requerido)
    for valor in args:
        total+=valor
    return total

resultado = suma_args_param("Este es un argumento requerido",10,20,30,40,50,60)
print(resultado)

# se puede colocar n cantidad de argumentos tambien con doble asterisco **
# por convencion el nombre del parametro debe de ser kwargs
# el parametro kwargs es un diccionario
def usuarios_autenticados(**kwargs):
    print(kwargs)

usuarios_autenticados(codi=True,facilito=False)
"""
salida esperada
{'codi': True, 'facilito': False}
"""

def combinacion(requerido,*args,**kwargs):
    print(requerido)
    print(args)
    print(kwargs)

combinacion("Valor requerido",10,2,valor_uno=True,valor_dos=False)
#asigna por clave valor los kwargs
"""
Valor requerido
(10, 2)
{'valor_uno': True, 'valor_dos': False}
"""