# es un tipo especial de funcion que se puede utilizar para la creacion de una secuencia de datos
# datos que se pueden iterar
# secuencia que manda a retornar es una secuencia que no vamos a definir
# no se guarda en la ram

# la palabra yield 
# como funciona yield 
# retornar el resultado del for sin terminar la funcion tabla_multiplicar
# en cada iteracion retorna un valor
# luego se almacena en resultado
# en cada iteracion se genera el resultado
# se pueden retornar mas valor4es
def tabla_multiplicada(numero, maximo=10):
    for posicion in range(1,maximo+1):
        #yield numero * posicion
        yield numero * posicion, numero, posicion

for resultado,numero,posicion in tabla_multiplicada(9,5):
    print(numero, "*", posicion,"=",resultado)

"""
resultado
9
18
27
36
45
54
63
72
81
90

de la nueva iteracion con parametro
9 * 1 = 9
9 * 2 = 18
9 * 3 = 27
9 * 4 = 36
9 * 5 = 45
"""