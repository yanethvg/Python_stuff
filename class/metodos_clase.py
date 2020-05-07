# son metodos que pueden ser llamados sin necesidad de crear una instancia de la clase
# los metodos de clase deben de recibir un parametro obligatoriamente
#  por convencion cls se coloca
# cls hace referencia a la clase
# cuando se necesite utilizar variables de clase
class Circulo:
    pi = 3.14159265

    @classmethod
    def area(cls,radio):
        return cls.pi * radio**2


resultado = Circulo.area(10)
print(resultado)
