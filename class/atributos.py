# se pueden crear atributos dentro de la clase y fuera de la clase
class Usuario:
    def saluda(self, nombre):
        print("Hola, soy un usuario "+ nombre)

    def mostrar_username(self):
        print(self.username)

    def mostrar_nombre(self):
        print(self.nombre)

    #asignando por medio de metodos los atributos
    #creo atributos
    def crear_nombre(self,nombre):
        self.nombre = nombre

#haciendo instancias
#atributos declarados afuera de la clase
# self hace referencia al objeto
codi = Usuario()
codi.username='codi'
codi.email='codi.@gmail.com'

facilito = Usuario()
facilito.username='facilito'
facilito.email='facilito.@gmail.com'

#llamando la funcion
codi.mostrar_username()
facilito.mostrar_username()

#creando atributos por medio del metodo
codi.crear_nombre("Codigo")
#mostrar el atributo 
codi.mostrar_nombre()