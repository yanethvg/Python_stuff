def comenzar_play_list(lista):
    #esta haciendo uso de la variable lista
    def reproducir():
        # la variable es modificada de esta manera no ocupara la lista global
        # si que la lista definida dentro del namespace de def reproducir
        nonlocal lista
        lista = [1,2,3]
        for val in lista:
            print(val)
    
    reproducir()
    print(lista)
    

lista = ['track 1','track 2','track 3','track 4']
#al igual que las variables globales no se puede modificar la variable global
comenzar_play_list(lista)