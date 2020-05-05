#Listar todos los números pares del 0 al 100
for numero in range(1, 101):
    # si el reciduo es = 0
    # muestralo en pantalla.
    if numero % 2 == 0:
        # Formateando los datos de salida.
        print(f"\t\t{numero}")