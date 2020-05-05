numeros = [1,2,3,4,5,6,7,8,9,10]

for numero in numeros:
    print(numero)

#iterar un diccionario
diccionario = {'a': 1, 'b':2}
#las llaves del diccionario
for llave in diccionario:
    print(llave)

valores = ((10,20),["strings","strings"],(True,False))

for valor in valores:
    print(valor)

#se puede sacar los valores dentro de esta, se coloco los valores de acuerdo al numero de variables
for valor1,valor2 in valores:
    print(valor1,valor2)