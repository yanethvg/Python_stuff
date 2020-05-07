
class Animal:
    def __init__(self,nombre):
        self.nombre = nombre
    
    def comer(self):
        print("Comiendo")

    def dormir(self):
        print("Durmiendo")

#herencia por medio de parentesis
class Perro(Animal):
    def ladrar(self):
        print("Ladrando")

class Gato(Animal):
    def ronroneo(self):
        print("Ronroneo")

firulais = Perro("Firulais")
firulais.comer()
firulais.dormir()
firulais.ladrar()
print("\n")

gatito = Gato("Gatito")
gatito.comer()
gatito.dormir()
gatito.ronroneo()