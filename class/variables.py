# existen las variables de instancia y las variables de clase
# las variables de instancia le pertenecen a la instancia que la creo
# las variables de instancia no se comparten entre instancia
# las variables de clase le pertenecen a la clase
# pueden ser ocupadas por las instancias
class Circulo:
    pi = 3.14159265 # es una variable de clase
    def __init__(self,radio):
        self.radio = radio # es una variable de instancia por eso no se modifica

circulo_a = Circulo(10)
circulo_b = Circulo(20)

circulo_b.radio = 100

print(circulo_a.radio)
print(circulo_b.radio)
print("\n")
print(circulo_a.pi)
print(circulo_b.pi)
print("\n")
# se pueden utilizar estas variables de clase sin instanciar
print(Circulo.pi)