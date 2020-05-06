# Utilizando init para inicializar los atributos
class Usuario:

    def __init__(self,username='',email='',nombre=''):
        self.username = username
        self.email = email
        self.nombre = nombre

    def saluda(self):
        print("Hola, soy un usuario "+ self.nombre)

    def mostrar_username(self):
        print(self.username)

    def mostrar_nombre(self):
        print(self.nombre)
    #ya no es necesario este metodo para agregar
    """
    def crear_nombre(self,nombre):
        self.nombre = nombre
    """


codi = Usuario('codi','codi@gmail.com','codigo completo')
# ya no es necesario este tipo de asignacion
"""
codi.username='codi'
codi.email='codi.@gmail.com'
"""

facilito = Usuario('facilto','facilito@gmail.com','facilito')

codi.saluda()


