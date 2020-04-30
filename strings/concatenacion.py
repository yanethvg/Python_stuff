curso = "Curso de Python"
#generar un nuevo string ya que es inmutable
#no se puede concatenar si no string
curso = "c" + curso[1:] + str(3) +" "+ str(True) +" "+ "en codigo facilito."

print(curso)