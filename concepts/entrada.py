#print("¿Cual es tu nombre?")
nombre = input("¿Cual es tu nombre?\n")

#print("¿Cual es tu edad?")
edad = int(input("¿Cual es tu edad?\n"))

#print("¿Cual es tu peso?")
peso = float(input("¿Cual es tu peso?\n"))

#print("Estas autorizado?(si/no)")
autorizado = input("Estas autorizado?(si/no)\n") == "si"

print("Hola",nombre, "tu edad es: ", edad, " tu peso es: ",peso)
print("Autorizado",autorizado)