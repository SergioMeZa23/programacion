numeros=[]
import random

for i in range(20):
    n=random.randrange(40,350)
    numeros.append(n)
    print(n)

lista=input("ingrese un numero de la lista: ")
lista= int(lista)
contar=numeros.count(lista)
print(f"el numero elegido: {lista}, se repite {contar} veces")