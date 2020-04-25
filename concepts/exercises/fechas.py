from datetime import datetime

fecha = input("Ingrese la fecha de nacimiento\n")

date = datetime.strptime(fecha, '%m-%d-%Y').date()

now = datetime.now().date()

anios = now.year - date.year
meses = date.month - now.month
dias = date.day - now.day

if(meses < 0):
    meses_rest = abs(meses)
    anios = anios +1 

if(meses==0):
    meses_rest = 0
    if(dias<0):
        anios=anios-1

if(meses > 0):
    meses_rest = 12- meses
    anios = anios -1 

resultado = anios * 12 + abs(meses_rest)

print("años",anios)
print("meses", meses)
print("dias", dias)
print("Cantidad de meses: ",resultado)