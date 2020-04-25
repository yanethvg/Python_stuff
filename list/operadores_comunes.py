lista = [8.17, 90, 1, 5, 44, 1.32,5]
#para ordenar la lista de forma ascendente
lista.sort()
#para ordenar la lista de forma descendente
lista.sort(reverse=True)
#para obtener el mayor solo necesito ordenar descendente y el menos ascendente 
may = lista[0]

#para obtener el menor 
minimo= min(lista)
#para obtener el mayor 
mayor = max(lista)

#para conocer la longitud de la lista
longitud = len(lista)

#buscar un elemento en la lista
resultado = 8 in lista #devuelve boolean
resultado = 8.17 in lista

#encontrar el indice en donde se encuentra
indice = lista.index(5)

#para conocer cuantas veces sale un elemento en la lista
#si el elemento no se encuentra devuelve cero
contador = lista.count(5)

print(contador)

# vowels list
vowels = ['a', 'e', 'i', 'o', 'i', 'u']

# index of 'e'
index = vowels.index('i')
print('The index of i:', index)
