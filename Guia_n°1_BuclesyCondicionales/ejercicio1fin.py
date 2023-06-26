#ejercicio 1

print()
texto = "La Universidad de los Lagos es una institución estatal fundada en 1993. Esta universidad regional entrega una contribución significativa al desarrollo sostenible del territorio. Como Universidad sus pilares fundamentales se basan en la inclusión, pluralismo, conciencia ambiental y participación democrática."
print(texto.split())
print()
#contar cantidad de repeticiones de "universidad"
palabra=texto.count("Universidad")
palabra2=texto.count("universidad")
palabras=texto.count("Universidad")+texto.count("universidad")
print(f"La palabra universidad se repite {palabras} veces")
print()
print(f"La palabra Universidad se repite {palabra} veces, y la palabra universidad se repite {palabra2} vez")
print()

lista=[]
lista.append("Universidad")
lista.append("universidad")
print(lista)
tupla=tuple(lista)










print()