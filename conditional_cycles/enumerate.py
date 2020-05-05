#enumerate se puede recorer un objeto iterable
lista = [1,2,3,4,5,6]
#primer valor que comienza en cero y es entero
#segundo valor es el valor que almacena el objeto iterable
for indice,valor in enumerate(lista):
    print("indice:", indice, "valor:", valor)

# se puede indicar el punto de partida de la iteracion
for indice,valor in enumerate(lista,10):
    print("indice:", indice, "valor:", valor)