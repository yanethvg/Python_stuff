
class Animal:
    def __init__(self,nombre):
        self.nombre = nombre
    
    def comer(self):
        print("Comiendo")

    def dormir(self):
        print("Durmiendo")
    
    def comun(self):
        print("Este es un metodo de Animal")
    
# para sobreescribir un metodo se conoce como overrite
class Mascota:
    def fecha_adopcion(self,fecha):
        self.fecha_de_adopcion = fecha

    def comun(self):
        print("Este es un metodo de Mascota")
    
    
class Perro(Animal, Mascota):
    def ladrar(self):
        print("Ladrando")

    #sobreescribiendo la clase padre
    #colocando el metodo a sobreescribir
    #llamar la clase y su metodo y mandarle self
    def dormir(self):
        print(self.nombre, "esta durmiendo")
        #llamando el metodo de la clase padre
        Animal.dormir(self)
        print("No molestar")


class Gato(Animal, Mascota):
    def ronroneo(self):
        print("Ronroneo")


firulais = Perro("Firulais")
firulais.dormir()
