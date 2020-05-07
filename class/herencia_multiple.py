# como se lee de arriba hacia abajo
# se deben definir las clases antes que las clases hijas
class Animal:
    def __init__(self,nombre):
        self.nombre = nombre
    
    def comer(self):
        print("Comiendo")

    def dormir(self):
        print("Durmiendo")
    
    def comun(self):
        print("Este es un metodo de Animal")

# que sucede si hay un metodo en comun en ambas clases a heredar
class Mascota:
    def fecha_adopcion(self,fecha):
        self.fecha_de_adopcion = fecha

    def comun(self):
        print("Este es un metodo de Mascota")
    
    

#herencia por medio de parentesis
# se colocan separados por una coma
# busca de izquierda a derecha
# busca en la primera clase padre
# si no existe en la primera busca en la segunda y asi sucesivamente
class Perro(Animal, Mascota):
    def ladrar(self):
        print("Ladrando")
    #busca el metodos dentro de perro antes que en las demas
    """
    def comun(self):
        print("Este es un metodo de Perro")
    """

class Gato(Animal, Mascota):
    def ronroneo(self):
        print("Ronroneo")

firulais = Perro("Firulais")
firulais.comer()
firulais.dormir()
firulais.ladrar()
firulais.fecha_adopcion("Hoy")
print(firulais.fecha_de_adopcion)
firulais.comun()

print("\n")

gatito = Gato("Gatito")
gatito.comer()
gatito.dormir()
gatito.ronroneo()