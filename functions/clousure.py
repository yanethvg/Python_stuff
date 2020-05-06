"""
Explicacion
Cuando una funcion genere dinamicamente otra funcion 
esta nueva funcion puede acceder a las variables locales aun cuando
estas ya hayan sido finalizado
"""

def mostrar_mensaje(mensaje):
    mensaje = mensaje.title() #local lo hace local

    def mostrar():
        print(mensaje)
    
    return mostrar

nueva_funcion = mostrar_mensaje("CodigoFacilito")
nueva_funcion()