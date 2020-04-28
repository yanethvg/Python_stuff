tupla =(1,2,3,4,5,6)
#declarar varias variables en una sola linea de codigo
#uno,dos,tres,cuatro = tupla[0],tupla[1], tupla[2], tupla[3]
#se puede simplificar solamente declarando esto
#uno,dos,tres,cuatro = tupla
#si tiene mas elementos dara error porque debe tener la misma cantidad de elementos
#las variables declaradas en linea para evitar esto se coloca un asterisco en la 
#ultima variable

uno,dos,tres,*cuatro = tupla
print(uno)
print(dos)
print(tres)
print(cuatro)

"""
Salida esperada
1
2
3
[4, 5, 6]
"""
#el asterisco se puede poner en cualquiera de las variables e igual funciona

uno,*dos,cinco,seis = tupla
print(uno)
print(dos)
print(cinco)
print(seis)

"""
Salida esperada
1
[2, 3, 4]
5
6
"""
tupla =(1,2,3,4,5,6)
#se genera una nueva lista
lista = [10,20,30,40]
tupla_dos = (100,200,300,400)
#nos va a regresar un objeto de tipo zip puede recibir n cantidad de tuplas y n cantidad de listas
resultado = zip(tupla,lista,tupla_dos)
#pasando a ser una tupla
resultado = tuple(resultado)
#pasando a una lista
resultado = list(resultado)
print(resultado)


