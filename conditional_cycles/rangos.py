# range se puede crear una secuencia de numeros que se pueden iterar
#cuantos elementos se necesita
#siempre por defecto comienza de cero
#se coloca el numero de donde comiendo y el numero de terminacion (1,20) el ultimo numero no sale
for valor in range(1,20):
    print(valor)

#se puede trabajar con numeros negativos
for valor in range(-10,11):
    print(valor)

# se pueden colocar saltos
#se puede ver los numeros impares
for valor in range(1,101,2):
    print(valor)

lista = [1,2,3,4,5,6]
#se puede combinar con la funcion len
for indice in range(len(lista)):
    print('indice',indice, "valor:", lista[valor])
