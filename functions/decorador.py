#modificar una funcion existente sin modificar sus lineas de codigo
# se debe trabajar por lo menos con tres funciones
# a, b, c
# formula para crear un decorador
#a(b) -> c
# es para agregar codigo a una funcion 

def decorador(funcion):
    #pass # se utiliza para condicionales,ciclos o funciones indica no va a realizar nada
    #para pasar argumentos a la funcion que se ingresa como parametro del decorador
    # se agrega *args,**kwargs
    #todas las funciones retornan none por default
    #se retorna una tupla en una funcion cuando se envian varios valores
    # que nuevas caracteristicas quieres agregar a la funcion 
    # para evitar repetir codigo
    def nueva_funcion(*args,**kwargs):
        print("Podemos agregar codigo antes")
        resultado = funcion(*args,**kwargs)
        print("Podemos agregar codigo despues")
        return resultado

    return nueva_funcion

# para decorar se agrega el signo de @
@decorador
def funcion_a_decorar():
    print("Esta es una funcion a decorar")

# se decora correctamente
funcion_a_decorar()
print("\n")

@decorador
def suma(val1,val2):
    return val1 + val2

resultado = suma(10,20)
print(resultado)