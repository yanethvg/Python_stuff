# declarando metodos 
class Usuario:
    # todas las funciones deben de recibir un parametro
    # recibe self es una palabra reservada 
    # hace referencia al objeto en si
    # es obligatorio
    def saluda(self, nombre):
        print("Hola, soy un usuario "+ nombre)

#haciendo instancias
codi = Usuario()
facilito = Usuario()

#llamando la funcion
print(codi.saluda("Codi"))
print(facilito.saluda("Facilito"))