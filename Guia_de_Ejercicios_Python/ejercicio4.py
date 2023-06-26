
#ejercicio 4

nombre1 = input("ingrese el nombre de la primera persona: ")
nombre2 = input("ingrese el nombre de la segunda persona: ")
print("")

if nombre1[0] == nombre2[0]:
    print("ambos nombres empiezan con la misma letra")
    if nombre1[-1] == nombre2[-1]:print("ambos nombres terminan con la misma letra")
else:
    nombre1[0] != nombre2[0] and nombre1[-1] != nombre2[-1]
    print("no hay coincidencias")
print("")
print("")