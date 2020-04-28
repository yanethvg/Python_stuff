tupla = (1,2,3,4,5,6,7,8,9,0)

#obtener el elemento por medio de su indice
elemento = tupla[4]
#obtener elemento con indice negativo
elemento = tupla[-1]
#se puede crear subtuplas obtener los primeros 9 elementos con saltos de 2
subtupla = tupla[:9:2]
print(subtupla)
#modificar el elemento de una tupla esto no es posible porque son inmutables
