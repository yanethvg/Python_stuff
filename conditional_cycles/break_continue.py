titulo = "Curso de Python 3"

#finaliza el ciclo break
#terminar el ciclo
for caracter in titulo:
    if caracter == "P":
        break
    print(caracter)

#todos los caracteres exceptuando la letra P 
#saltar de iteracion
for caracter in titulo:
    if caracter == "P":
        continue
    print(caracter)