#los datos de entrada se van a conocer de parametros
def crear_mensaje(nombre):
    mensaje = "Hola {}, bienvenido al curso de python 3".format(nombre)
    #retornar el mensaje
    return mensaje

print(crear_mensaje("Zoila"))


#definir funciones con n cantidad de parametros con n cantidad de valores

def suma(val1,val2,val3):
    return val1 + val2 + val3

total = suma(2,3,10)

print("La suma total es: ", total)

#retornando 3 valores
def obtener_curso():
    return "Curso de Python","Basico", 3.6
#asignando a las variables en una sola linea
curso,nivel,version = obtener_curso()

print(curso,nivel,version)