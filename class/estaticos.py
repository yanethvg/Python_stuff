# metodos que se pueden usar sin la necesidad de usar la instancia

class Triangulo:
    numero = 2
    #haciendolo un metodo de instancia incluyendo self
    """
    def area(self):
        return (self.base *self.altura)/2
    """
    #decorar el metodo
    #se elimina self porque no pertenece a la instancia, se colocan las variables como parametro
    @staticmethod
    def area(base,altura):
        return (base * altura)/ Triangulo.numero

#al tener un metodo estatico ya no se necesita de crear la instancia
"""   
triangulo= Triangulo()
triangulo.altura = 20
triangulo.base = 10

resultado = triangulo.area()
"""
# se coloca la clase y se llama la funcion
# no podemos usar variables de instancia al usar metodos estaticos
#se pueden usar variables de clase
# recordar que las variables de clase primero se pone la clase luego su variable
resultado = Triangulo.area(10,20)
print(resultado)