palindromos = []

print("Teclea 4 frase, ¿Cual es palindromo?")
count = 1
while count <= 4:
    frase = input("Frase--> ")
    #print(frase[::-1]) le da la vuelta a la frase
    if frase == frase[::-1]: #palind_frase:
        palindromos.append(frase)
    else:
        print("Lo siento, no es palindromo")
    count += 1

print("")
print("Los palindromos son los siguientes")
for palindromo in palindromos:
    print(palindromo)